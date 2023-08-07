import instaloader

def get_instagram_user_info(username):
    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        print(f"Username: {username}")
        print(f"Number of Posts: {profile.mediacount}")
        print(f"Number of Followers: {profile.followers}")
        print(f"Number of Following: {profile.followees}")
        print(f"Description: {profile.biography}")

    except instaloader.exceptions.ProfileNotExistsException as e:
        print(f"Error: Profile '{username}' does not exist.")
    except instaloader.exceptions.PrivateProfileNotFollowedException as e:
        print(f"Error: Profile '{username}' is private and not followed.")
    except Exception as e:
        print("Error: Unable to fetch data.")
        print(e)

if __name__ == "__main__":
    username_input = input("Enter Instagram username: ")
    get_instagram_user_info(username_input)
