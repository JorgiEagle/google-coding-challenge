"""A video player class."""

from .video_library import VideoLibrary
from .video import Video
from random import randint


class VideoPlayer:
    """A class used to represent a Video Player."""

    video_playing = None
    video_paused = False

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        videos = []
        for video in self._video_library.get_all_videos():
            videos.append([video.title, video.video_id, video.tags])
        for video in sorted(videos, key=lambda x: x[0]):
            tag = '['
            if video[2]:
                for tags in video[2]:
                    tag += tags + ' '
            print(video[0], "("+video[1]+")", tag.rstrip() + ']', sep=' ')

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        if self.video_playing:
            self.stop_video()
        self.video_playing = self._video_library.get_video(video_id).video_id
        print('Playing video: ' + self._video_library.get_video(video_id).title)
        self.video_paused = False

    def stop_video(self):
        """Stops the current video."""

        print("Stopping video: " + self._video_library.get_video(self.video_playing).title) if self.video_playing else \
            print("Cannot stop video: No video is currently playing")
        self.video_playing = None
        self.video_paused = False

    def play_random_video(self):
        """Plays a random video from the video library."""
        if self.video_playing:
            self.stop_video()
        if not len(self._video_library.get_all_videos()):
            print('No videos available')
            return
        random_video = randint(0, len(self._video_library.get_all_videos())-1)
        self.play_video(self._video_library.get_video(self._video_library.get_all_videos()[random_video].video_id).
                        video_id)

    def pause_video(self):
        """Pauses the current video."""
        if not self.video_playing:
            print("Cannot pause video: No video is currently playing")
            return
        if not self.video_paused:
            print("Pausing video: " + self._video_library.get_video(self.video_playing).title)
            self.video_paused = True
        else:
            print("Video already paused " + self._video_library.get_video(self.video_playing).title)

    def continue_video(self):
        """Resumes playing the current video."""
        if not self.video_playing:
            print("Cannot continue video: No video is currently playing")
            return
        if self.video_paused:
            print("Continuing video: " + self._video_library.get_video(self.video_playing).title)
            self.video_paused = False
        else:
            print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        if not self.video_playing:
            print("No video is currently playing")
        else:
            video = self._video_library.get_video(self.video_playing)
            tag = '['
            for tags in video.tags:
                tag += tags + ' '
            print("Currently playing:", video.title, "("+video.video_id+")", tag.rstrip() + ']', sep=' ')

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
