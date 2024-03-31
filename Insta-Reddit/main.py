import insta_post
import reddit
count=0
#credentials for the accounts
list_credentials = ["email","password"]
list_credentials_2 = ["email2","password2"]

def setup(url,folder):
    """
    Using the url input and the folder destination.
    this function will search throurth the reddit for video urls
    the download the video in the folder
    """
    list_video = reddit.video_reddit(url)
    reddit.reset_videos()
    print(list_video)
    for element in list_video:
        reddit.download_file(element[0],element[1],folder)
    return list_video

list_video = setup("https://www.reddit.com/r/funnyvideos/",
                   ".\\videos")

def task():
    """
    Processes throught the list_video and logins and posts and captions then on instagram
    """
    filename = ".\\videos"
    if len(list_video):
        list_video = reddit.clean_up_folder(filename
                                            ,list_video)
        insta_post.post_on_insta(list_video.pop(0),list_credentials,filename)
    else:
        list_video = reddit.video_reddit("https://www.reddit.com/r/funnyvideos/")
        reddit.reset_videos()
        reddit.download_file(list_video[0],list_video[2]
                             ,filename)


list_video2 = setup("https://www.reddit.com/r/FunnyAnimals/",
                    ".\\videos2")

def task2():
    """
    SAME AS TASK()
    """
    filename =".\\videos2"
    if len(list_video2):
        list_video2 = reddit.clean_up_folder(filename,
                                             list_video2)
        insta_post.post_on_insta(list_video2.pop(0),list_credentials,filename)
    else:
        list_video2 = reddit.video_reddit("https://www.reddit.com/r/FunnyAnimals/")
        reddit.reset_videos()
        reddit.download_file(list_video2[0],list_video2[2]
                             ,filename)

task()
task2()