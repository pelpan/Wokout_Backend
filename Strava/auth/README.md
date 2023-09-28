## Get Strava API access token (full permission)

1. Create a [Strava API Application](https://www.strava.com/settings/api)
2. Get the `client_id` from api page.
3. Get **code**
   Open `https://www.strava.com/oauth/authorize?client_id=${your_id}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read_all,profile:read_all,activity:read_all,profile:write,activity:write` in your browser and accept the permissions. (replace `${your_id}` with your `client_id`)
   The `code` is in the url after you accept the permissios, which can only be used once.
4. Requests for access token.
