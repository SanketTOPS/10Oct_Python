import instaloader

name=input("Enter instagram id:")

insta=instaloader.Instaloader()

#insta.download_profile(name,profile_pic_only=True)
insta.download_profile(name,profile_pic_only=False)

print("Download Successfully!")