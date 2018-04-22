import shutil, os, time


# File Merge Program - Collects files from a drop, then sorts it into the destination
# Version 1.1.0.
# ------------------Beginning of Program ------------------------
print('Initializing...')
# Paths
surfacePc = 'C:/Users/nokot/Desktop/Drop/'
workstationPc = 'C:/Users/Tyler/Desktop/Drop/'
USB = 'D:/Python/'
USBText = 'D:/Python/Texts/'
USBPy = 'D:/Python/Scripts/'


def move(src, dst):
    # Checks whether the path is active to start process
    if os.path.exists(src):
        files = os.listdir(src)
        total = len(os.listdir(src))
        current_file_num = 1
        num_of_files = total
        # If the file is in the destination, skip
        for i in files:
            if os.path.exists(dst+i):
                print('{} exists in {} currently'.format(i, dst))
                current_file_num += 1
                pass
            # If file is not in destination, move there
            else:
                print('Transferring {} {}/{}'.format(i, current_file_num, num_of_files))
                shutil.move(src+i, dst)
                current_file_num += 1
                # All legible files should be transferred to initial destination


if __name__ == '__main__':
    while True:
        command = input('Please give a command...\n> ')
        if 'sync'.lower() in command:
            print('Starting Up Transfer\n')
            time.sleep(0.5)
            # Checking which path to sync data from
            if os.path.exists(surfacePc):
                move(surfacePc, USB)
                # Redirecting files to their appropriate places within destination
                for f in os.listdir(USB):
                    if f.endswith('txt'):
                        shutil.move(USB+f, USBText)

                    if f.endswith('py'):
                        shutil.move(USB+f, USBPy)

            else:
                move(workstationPc, USB)
                # Redirecting files to their appropriate places within destination
                for f in os.listdir(USB):
                    if f.endswith('txt'):
                        shutil.move(USB + f, USBText)

                    if f.endswith('py'):
                        shutil.move(USB + f, USBPy)

            print('Complete')
            time.sleep(1)
            break

        elif 'quit' in command:
            break
        else:
            print('List of commands are:\n"Sync"\n')
