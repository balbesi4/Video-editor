from AddCommand import AddCommand
from CopyFragmentCommand import CopyFragmentCommand
from CropPIctureCommand import CropPictureCommand
from ChangeSpeedCommand import ChangeSpeedCommand
from ChangeVolumeCommand import ChangeVolumeCommand
from ConcatenateCommand import ConcatenateCommand
from CropClipCommand import CropClipCommand
from FadeInCommand import FadeInCommand
from FadeOutCommand import FadeOutCommand
from Fragment import Fragment
from MirrorCommand import MirrorCommand
from RemoveAudioCommand import RemoveAudioCommand
from RemoveFragmentCommand import RemoveFragmentCommand
from ReverseCommand import ReverseCommand
from RotateClipsCommand import RotateClipsCommand
from SetAudioCommand import SetAudioCommand
from SplitClipCommand import SplitClipCommand
from SwapClipsCommand import SwapClipsCommand
from UploadImageClipCommand import UploadImageClipCommand
from UploadVideoClipCommand import UploadVideoClipCommand
import moviepy.editor as mp
import moviepy.video.fx.all as vfx
import os
import cv2


class TimeLine:
    def __init__(self):
        self.time_line = []
        self.changes = []

    def add(self, fragment: Fragment):
        add_command = AddCommand(self, fragment)
        self.changes.append(add_command)
        add_command.execute()

    def update_ids(self):
        current_id = 0
        for fragment in self.time_line:
            fragment.id = current_id
            current_id += 1

    def change_speed(self, multiplier, fragment_id: int):
        change_speed_command = ChangeSpeedCommand(self, multiplier, self.time_line[fragment_id])
        self.changes.append(change_speed_command)
        change_speed_command.execute()

    def change_volume(self, multiplier, fragment_id: int):
        change_volume_command = ChangeVolumeCommand(self, multiplier, self.time_line[fragment_id])
        self.changes.append(change_volume_command)
        change_volume_command.execute()

    def crop_clip(self, start, end, fragment_id: int):
        crop_clip_command = CropClipCommand(self, start, end, self.time_line[fragment_id])
        self.changes.append(crop_clip_command)
        crop_clip_command.execute()

    def concatenate(self, *fragment_ids: int, smooth=False, duration=None):
        fragments = [fragment for fragment in self.time_line if fragment.id in fragment_ids]
        concat_command = ConcatenateCommand(self, *fragments, smooth=smooth, duration=duration)
        self.changes.append(concat_command)
        concat_command.execute()

    def fade_in(self, fragment_id: int, duration):
        fade_in_command = FadeInCommand(self, duration, self.time_line[fragment_id])
        self.changes.append(fade_in_command)
        fade_in_command.execute()

    def fade_out(self, fragment_id: int, duration):
        fade_out_command = FadeOutCommand(self, duration, self.time_line[fragment_id])
        self.changes.append(fade_out_command)
        fade_out_command.execute()

    def upload_video_clip(self, path: str):
        upload_vc_command = UploadVideoClipCommand(self, path)
        self.changes.append(upload_vc_command)
        upload_vc_command.execute()

    def upload_image_clip(self, path: str, duration):
        upload_ic_command = UploadImageClipCommand(self, path, duration=duration)
        self.changes.append(upload_ic_command)
        upload_ic_command.execute()

    def set_audio(self, audio_path, fragment_id: int, full=False):
        set_audio_command = SetAudioCommand(self, audio_path, self.time_line[fragment_id], full)
        self.changes.append(set_audio_command)
        set_audio_command.execute()

    def swap_clips(self, fragment_1_id: int, fragment_2_id: int):
        swap_clips_command = SwapClipsCommand(self, self.time_line[fragment_1_id],
                                              self.time_line[fragment_2_id])
        self.changes.append(swap_clips_command)
        swap_clips_command.execute()

    def rotate_clips(self, *fragment_ids: int, angle=0):
        fragments = [fragment for fragment in self.time_line if fragment.id in fragment_ids]
        rotate_clips_command = RotateClipsCommand(*fragments, angle=angle)
        self.changes.append(rotate_clips_command)
        rotate_clips_command.execute()

    def crop_clip_picture(self, fragment_id: int, x1=0, y1=0, x2=0, y2=0):
        crop_picture_command = CropPictureCommand(self.time_line[fragment_id], x1, y1, x2, y2)
        self.changes.append(crop_picture_command)
        crop_picture_command.execute()

    def reverse(self, fragment_id: int):
        reverse_command = ReverseCommand(self.time_line[fragment_id])
        self.changes.append(reverse_command)
        reverse_command.execute()

    def remove_audio(self, *fragment_ids: int):
        fragments = [fragment for fragment in self.time_line if fragment.id in fragment_ids]
        remove_audio_command = RemoveAudioCommand(*fragments)
        self.changes.append(remove_audio_command)
        remove_audio_command.execute()

    def split_clip(self, fragment_id: int, split_time):
        split_clip_command = SplitClipCommand(self, self.time_line[fragment_id], split_time)
        self.changes.append(split_clip_command)
        split_clip_command.execute()

    def copy_fragment(self, fragment_id: int):
        copy_fragment_command = CopyFragmentCommand(self, self.time_line[fragment_id])
        self.changes.append(copy_fragment_command)
        copy_fragment_command.execute()

    def mirror(self, fragment_id, x):
        mirror_command = MirrorCommand(x, self.time_line[fragment_id])
        self.changes.append(mirror_command)
        mirror_command.execute()

    def export(self, name: str, fps, width, height, gif=False):
        final_clips = [fragment.clip.fx(vfx.resize, width=width, height=height) for fragment in
                       self.time_line]
        clip_to_export = mp.concatenate_videoclips(final_clips)
        if not gif:
            clip_to_export.write_videofile(name, fps)
        else:
            clip_to_export.write_gif(name, fps)
        clip_to_export.close()

    def count(self):
        return len(self.time_line)

    def remove(self, *fragment_ids: int):
        remove_command = RemoveFragmentCommand(self, *fragment_ids)
        self.changes.append(remove_command)
        remove_command.execute()

    def undo(self):
        last_change = self.changes.pop()
        last_change.undo()
