Links: [[00 - Global Index (Start Here!)]] [[03 - Try Hack Me]] [[Active Directory]] [[Attacking Kerberos]]
# [01 - Introduction]
## Notes
---
What is Kerberos?

deafult auth service for windows and is more "secure" the NTLM

Common Terms:
- Ticket Granting Ticket (TGT) - A ticket-granting ticket is an auth ticket used to request service tickets from the TGS
- Key Distribution Center (KDC) the KDC is a service for issuing a TGT and service tickets that consist of the Auth serice and TGS
- Auth Service (AS) - Issues TGT to be used by the TGS in the domain to request access to other machines and service tickets
- Ticket Granting Service (TGS) - Takes a TGT and returns a ticket to a machine on the domain
- Service Principal Name (SPN) - SPN is an identifier given to a service instance to associate a service instanc ewith a domain service account. Windows requires that services have a domain service account which is why a service needs an SPN set.
- KDC Long Term Secret Key (KDC LT Key) - The KDC key is based on the KRBTGT service account. It is used to encrypt the TGT and sign the PAC
- Client Long Term Secret Key (Client LT Key) - The client key is based on the computer or service account. It is used to check the encryption timestamp and encrypt the session key
- Service Long Term Secret Key (Service LT Key) - The service key is based on the service account. It is used to encrypt the service portion of the service ticket and sign the PAC.
- Session Key - Issued bu the KDC when a TGT is issued. The suer will provide the session key to the KDC along with the TGT when requesting a service ticket
- Privilege Attribute Certificate (PAC) - The PAC holds all of the user's relevant information. is sent with the TGT to the KDC to be signed by the Target LT Key and the KDC LT Key in order to validate the user.


AS-REQ with pre-auth in detail.

AS-REQ in kerberos auth starts when a user requests a TGT from the KDC. In order to validate the user and create a TGT the KDC follows these step.
- User encrypts a timestamp NT hash and sends it to the AS.
- The KDC attempts to decrypt the timestamp using the NT hash from the user.
- The KDC will give a TGT and a session key for the user.

Ticket Granting Ticket Contents

the TGT is provided by the user to the KDC -> KDC vsalidates the TGT and gives back a service ticket

Service Ticket Contents
Two portions
Service: User Details, Session Key, Encrypts the ticket with the service account NTLM hash.
User: Validity Timestamp, Session Key, Encrupts with the TGT session key

Kerberos Authentication Overview:

AS-REQ - 1). The client requests an Authentication Ticket or TGT
AS-REP - 2). The Key Distribution Center verifies the client and sends back an encrypted TGT
TGS-REQ - 3). Client sends the encrypted TGT to the TGS with the SPN of the service the client wants to access.
TGS-REP - 4). The KDC verifies the TGT of the user and that the user has access to the service, then sends a valid session key for the service to the client.
AP-REQ -5). the client requests the service and sends the valid session key to prove the user has access.
AP-REP - 6). the service grants access.

Attack Privilege Requirements
- Kerbrute Enumeration - No doamin access required
- Pass the Ticket - Access as a user to the domain required
- Kerberoasting - Access as any user required
- AS-REP Roasting - Access as any user required
- Golden Ticket - Full domain compromise (DA) required
- Silver Ticket - Service hash required
- Skeleton Key - Full domain compromise (DA) requried