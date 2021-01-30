# Template for showing a progress bar while performing slow tasks
import unreal

total_frames = 100
text_label = "Working!"
with unreal.ScopedSlowTask(total_frames, text_label) as slow_task:
    slow_task.make_dialog(True)               # Makes the dialog visible, if it isn't already
    for i in range(total_frames):
        if slow_task.should_cancel():         # True if the user has pressed Cancel in the UI
            break
        slow_task.enter_progress_frame(1)     # Advance progress by one frame.
                                              # You can also update the dialog text in this call, if you want.
        #...                                  # Now do work for the current frame here!