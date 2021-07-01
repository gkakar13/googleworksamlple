"""A video player class."""

from .video_library import VideoLibrary
import numpy as np

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playing= 'No'
        self._paused= 'No'
        self._playlists=[]
        
    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")


    def print_video_info(self, video_id) :
        print((VideoLibrary.get_video(self._video_library, video_id).title),end = ' (')
        print(VideoLibrary.get_video(self._video_library, video_id).video_id, end=') ')
        print('[', end='')
        for i in range(len(VideoLibrary.get_video(self._video_library, video_id).tags)):
            if i!=len(VideoLibrary.get_video(self._video_library, video_id).tags) - 1:
                print(VideoLibrary.get_video(self._video_library, video_id).tags[i],end=' ')
            else:
                print(VideoLibrary.get_video(self._video_library, video_id).tags[i],end=']')

    def show_all_videos(self):
        """Returns all videos."""
        
        print("Here's a list of all available videos:")
        strings_list=[]

        for vid in self._video_library.get_all_videos():
            str_temp_list=[]
            str_temp_list.append((vid.title+' ('+vid.video_id+')'+" ["))
            for i in range(len(vid.tags)):
                str_temp_list.append(vid.tags[i])
                if i!=len(vid.tags)-1:
                    str_temp_list.append(' ')
            str_temp_list.append(']')
            separator=''
            strings_list.append(separator.join(str_temp_list))
         
        for line in (np.sort(strings_list)):
            print(line)
        
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        
        video_id_valid=False
        for video in self._video_library.get_all_videos():
            if video.video_id==video_id:
                video_id_valid=True
                break
        
        
        if video_id_valid==False:
            print('Cannot play video: Video does not exist',end='')
        else:
            if self._playing!= 'No':
                print('Stopping video: '+str(VideoLibrary.get_video(self._video_library,self._playing).title))
                
            if self._paused!='No':
                print('Stopping video: '+ str(VideoLibrary.get_video(self._video_library, self._paused).title))
                
            print('Playing video: '+str(VideoLibrary.get_video(self._video_library,video_id).title))
            self._playing=video_id
            self._paused='No'   
        
    def stop_video(self):
        """Stops the current video."""       
            
        if self._playing != 'No':
            print('Stopping video: '+ str(VideoLibrary.get_video(self._video_library, self._playing).title))
            self._playing= 'No'
        elif self._paused != 'No':
            print('Stopping video: '+ str(VideoLibrary.get_video(self._video_library, self._paused).title))
            self._paused= 'No'
        else:
            print('Cannot stop video: No video is currently playing')
        

    def play_random_video(self):
        """Plays a random video from the video library."""
        
        videos_list=self._video_library.get_all_videos()
        videos_num= len(videos_list)
        random_video_num=np.random.randint(0,videos_num)
        
        if self._playing!='No':
            print('Stopping video: '+ str(VideoLibrary.get_video(self._video_library, self._playing).title))
        
        if self._paused!='No':
            print('Stopping video: '+ str(VideoLibrary.get_video(self._video_library, self._paused).title))
        
        print('Playing video: '+str(videos_list[random_video_num].title))
        self._playing=videos_list[random_video_num].video_id
        self._paused='No'

    def pause_video(self):
        """Pauses the current video."""
        
        if self._playing=='No':
            if self._paused=='No':
                print('Cannot pause video: No video is currently playing')
            else:
                print('Video already paused: ' +str(VideoLibrary.get_video(self._video_library,self._paused).title))
        else:
            print('Pausing video: '+str(VideoLibrary.get_video(self._video_library,self._playing).title))
            self._paused=self._playing
            self._playing='No'
            
            
    def continue_video(self):
        """Resumes playing the current video."""

        if self._paused!='No':
            print('Continuing video: '+str(VideoLibrary.get_video(self._video_library,self._paused).title))
            self._playing=self._paused
            self._paused='No'
        elif self._playing!='No':
            print('Cannot continue video: Video is not paused')
        else:
            print('Cannot continue video: No video is currently playing')

    def show_playing(self):
        """Displays video currently playing."""
        
        if self._playing!='No':
            print('Currently playing: '+str(VideoLibrary.get_video(self._video_library, self._playing).title),end=' (')
            print(VideoLibrary.get_video(self._video_library, self._playing).video_id, end=') ')
            print('[', end='')
            for i in range(len(VideoLibrary.get_video(self._video_library, self._playing).tags)):
                if i!=len(VideoLibrary.get_video(self._video_library, self._playing).tags) - 1:
                    print(VideoLibrary.get_video(self._video_library, self._playing).tags[i],end=' ')
                else:
                    print(VideoLibrary.get_video(self._video_library, self._playing).tags[i],end=']')

            
        elif self._paused!='No':
            print('Currently playing: '+str(VideoLibrary.get_video(self._video_library, self._paused).title),end=' (')
            print(VideoLibrary.get_video(self._video_library, self._paused).video_id, end=') ')
            print('[', end='')
            for i in range(len(VideoLibrary.get_video(self._video_library, self._paused).tags)):
                if i!=len(VideoLibrary.get_video(self._video_library, self._paused).tags) - 1:
                    print(VideoLibrary.get_video(self._video_library, self._paused).tags[i],end=' ')
                else:
                    print(VideoLibrary.get_video(self._video_library, self._paused).tags[i],end=']')

            print(' - PAUSED')
        else:
            print('No video is currently playing')
            
    def playlist_exists_and_location(self,playlist_name):
        playlist_name_taken=False
        for playlist_ind in range(len(self._playlists)):
            if self._playlists[playlist_ind][0].upper()==playlist_name.upper():
                playlist_name_taken=playlist_ind
                break
        return(playlist_name_taken)
        
    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        
        playlist_name_taken=False
        for playlist in self._playlists:
            if playlist[0].upper()==playlist_name.upper():
                playlist_name_taken=True
                break
        if playlist_name_taken:
            print('Cannot create playlist: A playlist with the same name already exists')
        else:
            print('Successfully created new playlist: '+playlist_name)
            self._playlists.append([playlist_name])

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        
        playlist_exists=False
        for ind in range(len(self._playlists)):
            if self._playlists[ind][0].upper()==playlist_name.upper():
                playlist_exists=True
                playlist_ind=ind
                break
        
        video_id_valid=False
        for video in self._video_library.get_all_videos():
            if video.video_id==video_id:
                video_id_valid=True
                break
        
        if not playlist_exists:
            print('Cannot add video to '+playlist_name+': Playlist does not exist')
        else:
            vid_already_in_playlist=False
            for vid_id in self._playlists[playlist_ind]:
                if vid_id==video_id:
                    vid_already_in_playlist=True
                    break
            if not video_id_valid:
                print('Cannot add video to '+playlist_name+': Video does not exist')
            elif vid_already_in_playlist:
                print('Cannot add video to '+playlist_name+': Video already added')
                
            else:
                print('Added video to '+playlist_name+': '+str(VideoLibrary.get_video(self._video_library, video_id).title))
                self._playlists[playlist_ind].append(video_id)
            
    def show_all_playlists(self):
        """Display all playlists."""

        if self._playlists==[]:
            print('No playlists exist yet')
        else:
            print('Showing all playlists:')
            playlist_names=[]
            for playlist in self._playlists:
                playlist_names.append(playlist[0])
            for playlist_name in np.sort(playlist_names):
                print(playlist_name)
                
    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
       
        playlist_exists=False
        for ind in range(len(self._playlists)):
            if self._playlists[ind][0].upper()==playlist_name.upper():
                playlist_exists=True
                playlist_ind=ind
                break
        if not playlist_exists:
            print('Cannot show playlist '+playlist_name+': Playlist does not exist')
        else:
            print('Showing playlist: '+playlist_name)
            if len(self._playlists[playlist_ind])==1:
                print('No videos here yet')
            else:
                for vid_ind in range(1,len(self._playlists[playlist_ind])):
                    self.print_video_info(self._playlists[playlist_ind][vid_ind])
                    print('\n',end='')



    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        
        video_id_valid=False
        for video in self._video_library.get_all_videos():
            if video.video_id==video_id:
                video_id_valid=True
                break
        
        playlist_ind=self.playlist_exists_and_location(playlist_name)
        if type(playlist_ind)==bool and playlist_ind==False:
            print('Cannot remove video from '+playlist_name+': Playlist does not exist')
        else:
            if video_id_valid==False:
                print('Cannot remove video from '+playlist_name+': Video does not exist')
            else:
                video_exists=False
                for vid_id in self._playlists[playlist_ind]:
                    if vid_id==video_id:
                        video_exists=True
                        break
                if not video_exists:
                    print('Cannot remove video from '+playlist_name+': Video is not in playlist')
                else:
                    print('Removed video from '+playlist_name+': '+str(VideoLibrary.get_video(self._video_library, video_id).title))
                    self._playlists[playlist_ind].remove(video_id)
                
                
        
    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_ind=self.playlist_exists_and_location(playlist_name)
        if type(playlist_ind)==bool and playlist_ind==False:
            print('Cannot clear playlist '+playlist_name+': Playlist does not exist')
        else:
            self._playlists[playlist_ind].clear()
            self._playlists[playlist_ind].append(playlist_name)
            print('Successfully removed all videos from '+playlist_name)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_ind=self.playlist_exists_and_location(playlist_name)
        if type(playlist_ind)==bool and playlist_ind==False:
            print('Cannot delete playlist '+playlist_name+': Playlist does not exist')
        else:
            self._playlists.pop(playlist_ind)
            print('Deleted playlist: '+playlist_name)

    
    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

        search_result_ids=[]
        
        for video_object in self._video_library.get_all_videos():
            if search_term.lower() in video_object.title.lower():
                search_result_ids.append(video_object.video_id)
        if search_result_ids==[]:
            print('No search results for '+search_term)
        else:
            print('Here are the results for '+search_term+':')
            for i in range(len(search_result_ids)):
                print(str(i+1)+') ', end='')
                self.print_video_info(search_result_ids[i])
                print('\n',end='')
            print('Would you like to play any of the above? If yes, specify the number of the video.')
            print("If your answer is not a valid number, we will assume it's a no.")
            special_command=input('')
                        
            try:
                command_num=int(special_command)
                for i in range(len(search_result_ids)):
                    if command_num==(i+1):
                        self.play_video(search_result_ids[i])
            except ValueError:
                pass
            
    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """


        search_result_ids=[]
        
        for video_object in self._video_library.get_all_videos():
            for tag in video_object.tags:
                if tag.lower()==video_tag:
                    search_result_ids.append(video_object.video_id)
        
        if search_result_ids==[]:
            print('No search results for '+video_tag)
        else:
            print('Here are the results for '+video_tag+':')
            for i in range(len(search_result_ids)):
                print(str(i+1)+') ', end='')
                self.print_video_info(search_result_ids[i])
                print('\n',end='')
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            
            special_command=input('')
            try:
                command_num=int(special_command)
                for i in range(len(search_result_ids)):
                    if command_num==(i+1):
                        self.play_video(search_result_ids[i])
            except ValueError:
                pass
            
        
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
