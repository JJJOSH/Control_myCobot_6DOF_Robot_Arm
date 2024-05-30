from __future__ import print_function
from pymycobot.mycobot import MyCobot
import sys, termios, tty, time


def vels(sped, turn):
    return "currently:\tsped: %s\tchnge percent: %s  " % (sped, turn)


class Raw(object):
    def __init__(self, stream):
        self.stream = stream
        self.fd = self.stream.fileno()

    def __enter__(self):
        self.original_stty = termios.tcgetattr(self.stream)
        tty.setcbreak(self.stream)

    def __exit__(self, type, value, traceback):
        termios.tcsetattr(self.stream, termios.TCSANOW, self.original_stty)


def mycobot_pose_control():
    pc = MyCobot("/dev/ttyAMA0", 1000000)

    modl = 0
    sped = 50
    chnge_percent = 2

    chnge_angle = 180 * chnge_percent / 100
    chnge_len = 250 * chnge_percent / 100

 
hom_pose=[[0, 0, 0, 0, 0, 0],sped]
pick_pose=[[0, 30, 60, 80, 0, 45],sped]
place_pose=[[0, 0, 0, 0, 0, 0],sped]

    pc.send_angles(*hom_pose)

    while True:
        res = pc.get_coords()
        if res:
            break
        time.sleep(0.1)

    record_coords = [res, sped, modl]

    try:
      
        print(vels(sped, chnge_percent))
        while 1:
            try:
                print("\r current values of coords: %s" % record_coords)
                with Raw(sys.stdin):
                    key = sys.stdin.read(1)
                if key == "k":
                    pc.release_all_servos()
                    break
               elif key in "5":
    		    pc.send_angles(*pick_pose)
	       elif key in "6":
                    pc.send_angles(*place_pose)
               elif key in "7":
                    pc.send_angles(*hom_pose)
               elif key in "3":
                    rp = pc.get_angles()
                    hom_pose[0] =rp
                else:
                    continue

            except Exception as e:
                # print(e)
                continue

            time.sleep(1)

    except Exception as e:
        print(e)


def main():
    mycobot_pose_control()


if __name__ == "__main__":
    main()