from apns import APNs, Frame, Payload

token = 'A067C1FDF30CABD20035BADB898739510F3A5280E40261684E50F18C9B44C256'
payload = Payload(alert="This is your first notification", sound="default", badge=0)

apns = APNs(use_sandbox=True, cert_file='apns_pk.pem', key_file='apns_pk.pem')

apns.gateway_server.send_notification(token, payload)
