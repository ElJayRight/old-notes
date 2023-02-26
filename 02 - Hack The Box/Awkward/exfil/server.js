const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const jwt = require('jsonwebtoken')
const app = express()
const axios = require('axios')
const { exec } = require("child_process");
const path = require('path')
const sha256 = require('sha256')
const cookieParser = require("cookie-parser")
app.use(bodyParser.json())
app.use(cors())
app.use(cookieParser())
const mysql = require('mysql')
const { response } = require('express')
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'SQLDatabasePassword321!',
  database: 'hatvalley',
  stringifyObjects: true
})
const port = 3002

const TOKEN_SECRET = "123beany123"

app.post('/api/login', (req, res) => {
  const {username, password} = req.body
  connection.query(
    'SELECT * FROM users WHERE username = ? AND password = ?', [ username, sha256(password) ],
    function (err, results) {
      if(err) {
        return res.status(401).send("Incorrect username or password")
      }
      else {
        if(results.length !== 0) {
          const userForToken = {
            username: results[0].username
          }
          const firstName = username.split(".")[0][0].toUpperCase() + username.split(".")[0].slice(1).toLowerCase()
          const token = jwt.sign(userForToken, TOKEN_SECRET)
          const toReturn = {
            "name": firstName,
            "token": token
          }
          return res.status(200).json(toReturn)
        }
        else {
          return res.status(401).send("Incorrect username or password")
        }
      }
    }
  );
})

app.post('/api/submit-leave', (req, res) => {
  const {reason, start, end} = req.body
  const user_token = req.cookies.token
  var authFailed = false
  var user = null
  if(user_token) {
    const decodedToken = jwt.verify(user_token, TOKEN_SECRET)
    if(!decodedToken.username) {
      authFailed = true
    }
    else {
      user = decodedToken.username
    }
  }
  if(authFailed) {
    return res.status(401).json({Error: "Invalid Token"})
  }
  if(!user) {
    return res.status(500).send("Invalid user")
  }
  const bad = [";","&","|",">","<","*","?","`","$","(",")","{","}","[","]","!","#"] //https://www.slac.stanford.edu/slac/www/resource/how-to-use/cgi-rexx/cgi-esc.html

  const badInUser = bad.some(char => user.includes(char));
  const badInReason = bad.some(char => reason.includes(char));
  const badInStart = bad.some(char => start.includes(char));
  const badInEnd = bad.some(char => end.includes(char));

  if(badInUser || badInReason || badInStart || badInEnd) {
    return res.status(500).send("Bad character detected.")
  }

  const finalEntry = user + "," + reason + "," + start + "," + end + ",Pending\r"

  exec(`echo "${finalEntry}" >> /var/www/private/leave_requests.csv`, (error, stdout, stderr) => {
    if (error) {
      return res.status(500).send("Failed to add leave request")
    }
    return res.status(200).send("Successfully added new leave request")
  })
})

app.get('/api/all-leave', (req, res) => {
  const user_token = req.cookies.token
  var authFailed = false
  var user = null
  if(user_token) {
    const decodedToken = jwt.verify(user_token, TOKEN_SECRET)
    if(!decodedToken.username) {
      authFailed = true
    }
    else {
      user = decodedToken.username
    }
  }
  if(authFailed) {
    return res.status(401).json({Error: "Invalid Token"})
  }
  if(!user) {
    return res.status(500).send("Invalid user")
  }
  const bad = [";","&","|",">","<","*","?","`","$","(",")","{","}","[","]","!","#"] //https://www.slac.stanford.edu/slac/www/resource/how-to-use/cgi-rexx/cgi-esc.html

  const badInUser = bad.some(char => user.includes(char));

  if(badInUser) {
    return res.status(500).send("Bad character detected.")
  }

  exec("awk '/" + user + "/' /var/www/private/leave_requests.csv", {encoding: 'binary', maxBuffer: 51200000}, (error, stdout, stderr) => {
    if(stdout) {
      return res.status(200).send(new Buffer(stdout, 'binary'));
    }
    if (error) {
      return res.status(500).send("Failed to retrieve leave requests")
    }
    if (stderr) {
      return res.status(500).send("Failed to retrieve leave requests")
    }
  })
})

app.get('/api/store-status', async (req, res) => {
  await axios.get(req.query.url.substring(1, req.query.url.length-1))
    .then(http_res => {
      return res.status(200).send(http_res.data)
    })
    .catch(http_err => {
      return res.status(200).send(http_err.data)
    })
})

app.get('/api/staff-details', (req, res) => {
  const user_token = req.cookies.token
  var authFailed = false
  if(user_token) {
    const decodedToken = jwt.verify(user_token, TOKEN_SECRET)
    if(!decodedToken.username) {
      authFailed = true
    }
  }
  if(authFailed) {
    return res.status(401).json({Error: "Invalid Token"})
  }
  connection.query(
    'SELECT * FROM users', 
    function (err, results) {
      if(err) {
        return res.status(500).send("Database error")
      }
      else {
        return res.status(200).json(results)
      }
    }
  );
})

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname+'/readme.html'))
})

app.listen(port, 'localhost', () => {
  console.log(`Server listening on port ${port}`)
  connection.connect()
})

