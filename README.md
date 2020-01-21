Wallpaperify

Steps to get this working:
1. Go to https://developer.spotify.com/dashboard/applications and create a new application if you don't have one
2. Get your client id and client secret from your new App
3. Create a .env file in the gettokens folder and in there write the following (Remove the () and replace the insides with your variables )

CLIENT_ID=(Your_client_Id_here)
CLIENT_SECRET(Your_client_secret_here)

4. Run the main.py inside the gettokens folder, then go to http://localhost:8080 and follow the instructions presented there
5. After that, a .dotenvfile should've been generated. Copy it to the parent folder and rename it to .env
6. You're all set! Run main.py in the root folder and you Wallpaper should update every 60 seconds

Note: This is very WIP, PRs and issues are welcomed :D