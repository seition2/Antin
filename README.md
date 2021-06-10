client
dev tun
proto udp
sndbuf 0
rcvbuf 0
remote 18.202.129.195 1194
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
auth SHA512
cipher AES-256-CBC
comp-lzo
pull
key-direction 1
verb 3
reneg-sec 0
<ca>
-----BEGIN CERTIFICATE-----
MIIDKzCCAhOgAwIBAgIJANFm6rN7bVucMA0GCSqGSIb3DQEBCwUAMBMxETAPBgNV
BAMMCENoYW5nZU1lMB4XDTE4MTAwNjE3MjcxOVoXDTI4MTAwMzE3MjcxOVowEzER
MA8GA1UEAwwIQ2hhbmdlTWUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIB
AQCnB2awd18ddGk7tEZhDRTNSZdHR3rGJP6XopTBzf0hU4rqROarijVHVNhnoVLd
aq4aCbzXVLXPOoTEi8BOTeBquS6L6NKqJY+qFSeq1z40QjlnVZ034bw/AuWUtMzt
3FuPBbKd08KVas9GtHBa8XJ5a7K/a0Y/WGeGT3u3LBb4WO+imPBLrjJUSv2mwVY3
B8VRPiwRHFWCOV5uB0vjnmCQqzCnOlmtA+FOWg3M4eQoB+q2xldWFzlS4S3yh5/X
33gwYT1kPN1n7n0V62EOn+SfKYzzUZAH896By8tNLMEJVDZJrmHXf14X3uyT6eGd
0y7qzSkTKyRd/LmQnnmTLhrFAgMBAAGjgYEwfzAdBgNVHQ4EFgQUSjj+EgfxE9wW
/3XjMzfgR2RvKKAwQwYDVR0jBDwwOoAUSjj+EgfxE9wW/3XjMzfgR2RvKKChF6QV
MBMxETAPBgNVBAMMCENoYW5nZU1lggkA0Wbqs3ttW5wwDAYDVR0TBAUwAwEB/zAL
BgNVHQ8EBAMCAQYwDQYJKoZIhvcNAQELBQADggEBAJlVp7/eSFvQ5jTn3zTlr+ti
TriBX7KnnCQCy0WYC4//9R840JBUpsRX1mLnaw2sw4ScjiUALp7S0woZ7i4IfuVd
L7vA8iAVbeMWMiMYxmTbwb8yhis0y8UCS4PJNos5I1lgJC1mkrU4GsHrG5wB6afB
9kIJRJRHqusLOBXbuIwHm+Y7Z6cw1MT3dnUXBhdhy8VuSLFOgYhbDvguXC5hPdO7
Y64YifzWfeJ0i50U3Pf7NEw/l26YsTbUKBmLTozksFXaY2CfIAdZ+Z9damb0cAoK
KAnofFdgrtFHeiCTTwFaL+6uW8DSgsa7//PV6KWukNNzB0GgSt4V86A9UpDtgY8=
-----END CERTIFICATE-----
</ca>
<cert>
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            92:98:69:00:dd:1e:a2:f9:be:f4:01:6f:78:d7:b2:c4
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=ChangeMe
        Validity
            Not Before: Mar 14 22:01:10 2021 GMT
            Not After : Mar 12 22:01:10 2031 GMT
        Subject: CN=seition2
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:a6:14:8a:5b:7f:8b:9e:0a:15:f3:1a:f3:fe:de:
                    7c:91:d0:b6:0a:7a:ab:d4:06:e1:41:45:e4:d7:50:
                    52:e8:ef:c9:98:88:b6:dc:2f:58:3d:b7:52:b3:d8:
                    d5:18:09:8a:99:11:84:a4:da:90:9c:c6:a2:d9:d1:
                    a8:8d:25:b6:e1:63:e8:bb:08:d4:c4:38:b9:f1:18:
                    41:6c:b1:ea:92:19:ac:c3:1e:61:15:86:c4:64:36:
                    e8:9b:d0:30:1b:39:bb:b5:d6:f3:e9:72:a4:e5:86:
                    73:e0:30:8d:a3:c2:2b:e3:a6:c3:e3:9a:03:ca:35:
                    8f:a3:38:2b:62:6e:f3:45:2f:bb:5d:3b:b9:8f:55:
                    78:c1:80:86:cb:1a:98:bd:d9:67:e6:89:eb:18:a3:
                    a2:f9:0b:06:89:9b:25:7a:e6:df:d5:e3:ae:3b:0d:
                    4a:67:09:3f:b5:f5:fb:1b:33:3e:7d:a9:2d:0a:72:
                    ce:8f:81:21:98:86:99:a5:07:58:31:1f:9c:25:3f:
                    01:91:af:d6:03:9c:ad:0e:08:bf:13:e6:3e:a1:5d:
                    59:77:e9:d1:1c:c0:e4:05:70:31:bc:dc:8b:83:92:
                    e3:f5:69:a0:a9:48:20:08:bd:b6:19:19:20:b0:5d:
                    89:2f:90:4f:ab:91:95:10:2f:4e:6a:32:41:97:78:
                    6d:a9
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints: 
                CA:FALSE
            X509v3 Subject Key Identifier: 
                A9:F9:0B:F1:F0:1D:B3:27:28:FB:99:CC:2C:33:74:91:4A:EE:A6:D7
            X509v3 Authority Key Identifier: 
                keyid:4A:38:FE:12:07:F1:13:DC:16:FF:75:E3:33:37:E0:47:64:6F:28:A0
                DirName:/CN=ChangeMe
                serial:D1:66:EA:B3:7B:6D:5B:9C

            X509v3 Extended Key Usage: 
                TLS Web Client Authentication
            X509v3 Key Usage: 
                Digital Signature
    Signature Algorithm: sha256WithRSAEncryption
         79:00:81:bf:35:35:d0:9e:bc:a2:06:34:b6:d7:8d:63:9b:61:
         66:38:5f:68:ed:8f:b0:ba:31:e9:f4:59:cf:3f:89:2e:47:9e:
         ad:09:6f:d5:d3:89:a6:4d:0a:15:8f:2f:e8:1a:1e:fc:4d:75:
         39:94:70:58:69:98:24:c6:66:3b:d5:8c:d5:c2:bb:ef:fb:73:
         55:29:a0:50:9f:69:11:c0:3c:db:96:90:77:cb:7a:6d:3a:f8:
         fd:96:ba:bb:ee:86:7c:72:0b:7b:93:8a:06:e3:1b:cd:47:b4:
         ee:95:e5:71:08:8d:c8:70:e8:4d:e9:4b:6c:7d:d5:fc:89:03:
         54:1d:4c:75:1d:3d:d9:62:46:37:21:b5:c3:68:cb:92:fa:ae:
         3e:8c:b4:a5:18:6d:0b:d9:d4:2e:c5:7f:22:a7:dc:8e:66:8b:
         51:ba:4d:fc:95:69:31:4c:f3:93:61:85:d3:50:20:64:08:e6:
         ea:d5:bd:e1:a6:24:2c:0c:69:8d:81:8e:b0:7e:29:72:3c:84:
         16:ef:09:70:cf:6b:12:b0:03:c3:72:f5:09:b8:3b:4a:67:21:
         39:1a:f6:2b:7b:58:26:e0:85:7f:7c:8d:b6:7b:93:91:2b:34:
         08:a8:c2:95:26:95:65:65:44:b2:cc:e4:31:c2:e3:0c:80:03:
         0c:82:6b:a4
-----BEGIN CERTIFICATE-----
MIIDRjCCAi6gAwIBAgIRAJKYaQDdHqL5vvQBb3jXssQwDQYJKoZIhvcNAQELBQAw
EzERMA8GA1UEAwwIQ2hhbmdlTWUwHhcNMjEwMzE0MjIwMTEwWhcNMzEwMzEyMjIw
MTEwWjATMREwDwYDVQQDDAhzZWl0aW9uMjCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBAKYUilt/i54KFfMa8/7efJHQtgp6q9QG4UFF5NdQUujvyZiIttwv
WD23UrPY1RgJipkRhKTakJzGotnRqI0ltuFj6LsI1MQ4ufEYQWyx6pIZrMMeYRWG
xGQ26JvQMBs5u7XW8+lypOWGc+AwjaPCK+Omw+OaA8o1j6M4K2Ju80Uvu107uY9V
eMGAhssamL3ZZ+aJ6xijovkLBombJXrm39XjrjsNSmcJP7X1+xszPn2pLQpyzo+B
IZiGmaUHWDEfnCU/AZGv1gOcrQ4IvxPmPqFdWXfp0RzA5AVwMbzci4OS4/VpoKlI
IAi9thkZILBdiS+QT6uRlRAvTmoyQZd4bakCAwEAAaOBlDCBkTAJBgNVHRMEAjAA
MB0GA1UdDgQWBBSp+Qvx8B2zJyj7mcwsM3SRSu6m1zBDBgNVHSMEPDA6gBRKOP4S
B/ET3Bb/deMzN+BHZG8ooKEXpBUwEzERMA8GA1UEAwwIQ2hhbmdlTWWCCQDRZuqz
e21bnDATBgNVHSUEDDAKBggrBgEFBQcDAjALBgNVHQ8EBAMCB4AwDQYJKoZIhvcN
AQELBQADggEBAHkAgb81NdCevKIGNLbXjWObYWY4X2jtj7C6Men0Wc8/iS5Hnq0J
b9XTiaZNChWPL+gaHvxNdTmUcFhpmCTGZjvVjNXCu+/7c1UpoFCfaRHAPNuWkHfL
em06+P2WurvuhnxyC3uTigbjG81HtO6V5XEIjchw6E3pS2x91fyJA1QdTHUdPdli
RjchtcNoy5L6rj6MtKUYbQvZ1C7FfyKn3I5mi1G6TfyVaTFM85NhhdNQIGQI5urV
veGmJCwMaY2BjrB+KXI8hBbvCXDPaxKwA8Ny9Qm4O0pnITka9it7WCbghX98jbZ7
k5ErNAiowpUmlWVlRLLM5DHC4wyAAwyCa6Q=
-----END CERTIFICATE-----
</cert>
<key>
-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCmFIpbf4ueChXz
GvP+3nyR0LYKeqvUBuFBReTXUFLo78mYiLbcL1g9t1Kz2NUYCYqZEYSk2pCcxqLZ
0aiNJbbhY+i7CNTEOLnxGEFsseqSGazDHmEVhsRkNuib0DAbObu11vPpcqTlhnPg
MI2jwivjpsPjmgPKNY+jOCtibvNFL7tdO7mPVXjBgIbLGpi92WfmiesYo6L5CwaJ
myV65t/V4647DUpnCT+19fsbMz59qS0Kcs6PgSGYhpmlB1gxH5wlPwGRr9YDnK0O
CL8T5j6hXVl36dEcwOQFcDG83IuDkuP1aaCpSCAIvbYZGSCwXYkvkE+rkZUQL05q
MkGXeG2pAgMBAAECggEAblyr7E1/W8/b8iZxCWaTZNpKfgAyerzvps5pWWM5FS1y
y3fd+8dCXhCaVoS6ZjTA8yKfAGV1P5kH0rLtzI3JT1Fy8AbYTGRdu4agwzgfZmLF
WQuw+/sIOof6XsAjl5Pv1tA2WWUjipqkGdBp7u4y+B5zgaVw60hYYOAMhGayJcCW
NhfLjTenKd1PY+xdxyEBUGfFDeXJKkfm0zyrXVVrPWs1bOI+861HMXvJVCnixoaC
a6kHrY5BFf9LENCBz0qqpC1DV6q6pMbcAU9zWkSY9HNuyqhGmqc1REQL5EmxQhMq
lbL0a5g6r0fg8SheAuYW8cvzMdnbwH9QoG7Syzwv2QKBgQDP6xdx0yjmokw5GlB9
CWhMr4ksh1uAnXR8E4LGBboQCK+VRkAPYtKXDLC+EYq7seTbebD42SjVLz1+L50r
V92grhYZzovdupITPphZ6xPOR0CRb18KuTnSiPvc7kTkhsMOkOvBgd053GLe+JLK
KOoMOPQKWseFh5vRq4Gw10XwlwKBgQDMfJrlCE2CszeWg/aGw3BK4SxgVx3u+yRy
w9s5J5myr/NQS0X+zLKOeYturKUGg7cBLD3P46rBaVeVzBZAvfTD7B1yCbcIB8KK
PlqhOcB3tJnIMorKgofnS3f8lWAd5Sq1Tb7QgIRcvdDjFtRiGhczIe2h42NPcLc4
gtQNKKYbvwKBgQClbbfJqOjyGE/tXzKLSeDiowfRliEHxD/aOOvkAsp313Fco/h0
RXypEj/N+scXcANXXQuh86a5eEzFCb1TryV3owuSnPRMBxYSmcs+P/wSND77eFF2
hsmq6bL7pdjKuy6XeFccL+eFEgTYw46HquYNs4L4eiIl7C/eM0eNHLtZIQKBgQCx
Lp7AKUuQHl3iK4HnD10zZJyg9ZtYQYA5eP9xLKD+tXqsbiy+NPvae/KW+T0cwfBG
MeF1Sp3gbLiZcXcurelyAhsZftV7Pc4RHypEXNgqYPCHCVQ9WJENltTmpT/dZ350
DmNyIomOGmLvAg8Q2e6UPae8CF06rj3z11iJ9ljH3QKBgQDLXf5KhVuaQeiBih4n
BswsRVlgPlxd9ay/VWlKY3kGwuKNrvPtOZIm9madFZnGhZ2qKKU9JxIDi6TIPJPe
BIwJz2m/biis+D71NxfGZOBlChRSnFJWtzLcJY1fTWTuxOkXJNokWVp3FjGis+t1
YDOeI8DkwjvDCyK1gyLneAh9hQ==
-----END PRIVATE KEY-----
</key>
<tls-auth>
#
# 2048 bit OpenVPN static key
#
-----BEGIN OpenVPN Static key V1-----
9991d72fca8131e5735303b0df9c359f
80d8024794ad8145e9aee8506a534e30
d84c988fa96f18177f488cfe2d22635d
f84a717310d64134fb34485500af657e
833fe0e722adb689ca4b60916e286437
291cf395ae4309936b24c7953a73dc6b
2c0cbbef680d73dc1481eb81d09b5812
c48e54040e8732f45d1d0f8bfef1d83e
b79c721b1919c1587e05cb4287d8dd4e
d3d8e4e127ec12bd7c2f9ad59be5b92a
a32cc6e709318173ce236069cf6f36ba
64aff9f28506d3d2fd69d270dfda72d8
0b8a50ad7fd5722ab18e01fcd27a5a02
1b6d1b63c9caf115287c302148f0f5ac
303b9cbc7292856add10b20dca9919b3
10c1d0822841ba082a6831708683b39e
-----END OpenVPN Static key V1-----
</tls-auth>
