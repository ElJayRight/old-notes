# Set Gidbeon's PW
$pwd = ConvertTo-SecureString 'Password123#' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential('LicorDeBellora\Gibdeon',$pwd)
Add-AdGroupMember -Identity 'laps adm' -Members gibdeon -Credential $cred
Add-AdGroupMember -Identity 'laps read' -Members gibdeon -Credential $cred

