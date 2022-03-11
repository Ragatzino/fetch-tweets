# Fetch Tweets

Simple fetch tweet job for kubernetes

Parameters : 
- Bearer token for Twitter API : BEARER_TOKEN in env or .env.local file (not versionned)
- Subject of fetch request :  SUBJECT in env or .env or .env.local file

Fetches and output in stdout some tweets.

## Start app locally


1. Create Venv
```
python3 -m venv venv
```
(linux)

2. Init venv
```
source venv/bin/activate
```
(linux)

3. Install packages
```
pip install -r requirements.txt
```

4. Add your API key to .env.local

5. Launch App
```
python fetch-tweets.py
```

## Install with helm

Create a values file 
Add your API key to :
```yaml
secretname:
  bearer: <no-token-provided>
```
> chart/values.yaml

then

```
helm install --generate-name chart/
```