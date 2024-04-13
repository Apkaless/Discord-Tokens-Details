import base64
from DiscordTokens import token_validator

encrypted_token_ = 'd9UD5UtDYAyyRj2mFJhDbOOkVJ1UCL1i8VTBgBI0dKj0MAQZQ3SUw+qUFAWaPKUsaLUTdVu2BYJiah9ukCyEsOobPhvIZF3V5HUMhr8jYfHp1sSsibuqt0mT6eYxIv9h0dGWlw=='
# always starts with 'd'

token1 = "ODU5MjMzMDY2OTQ0ODIzMzE3.GQm4Zl.PofESIP3Wl6Twx_jzXiCzMxqYaHlHyZ4uyIrwMS"

token2 = 'NTQ2OTEwNjkzODI4NDYwNTg1.GBe6WR.IkFnGee2TlT-rypsijHrkyIwgp6nkb4z_--1Co'

token3 = 'MTAwMjE1NTA5ODkyMDcxODMzNg.GCaXv2.vHfrEwHIKfdo5ctcZeHe57JQJmyFu3bFLW9mXYN'

token4 = 'MTE1Nzc2MTA5OTI4Mjc5NjY4OA.G8QVTE.d_1l-XKWavqE998HGQT-C068qCKdm9pT7F6hj4'

print('Len of token 1: ', len(token1))
print('Len of token 2: ', len(token2))
print('Len of token 3: ', len(token3))
print('Len of token 4: ', len(token4))

dis_id1 = 'ODU5MjMzMDY2OTQ0ODIzMzE3.GQm4'  # token with prefix OD Takes the first 4 chars after the period (.) To Decode The Discord ID
dis_id2 = 'NTQ2OTEwNjkzODI4NDYwNTg1'       # token with prefix NT Takes No chars after the period (.) To Decode The Discord ID
dis_id3 = 'MTAwMjE1NTA5ODkyMDcxODMzNg.GC'  # token with prefix MT Takes the first 2 chars after the period (.) To Decode The Discord ID
dis_id4 = 'MTE1Nzc2MTA5OTI4Mjc5NjY4OA.G8'  # token with prefix MT Takes the first 2 chars after the period (.) To Decode The Discord ID

dec1 = base64.b64decode(dis_id1)
dec2 = base64.b64decode(dis_id2)
dec3 = base64.b64decode(dis_id3)
dec4 = base64.b64decode(dis_id4)

print('dec1: ', dec1)
print('dec2: ', dec2)
print('dec3: ', dec3)
print('dec4: ', dec4)

all_tokens = [token1, token2, token3, token4]

for token in all_tokens:
    resp = token_validator(token)
    print(resp)
