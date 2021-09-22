import math

PLOW_SPEED_MPS = 20/3.6 

def edge_length(a,b):
   return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def get_formatted_time_in_hours(time_in_seconds):
    hours = int(time_in_seconds//3600)
    minutes = (time_in_seconds%3600)/60
    minutes = round(minutes)
    if minutes == 60:
        minutes = 0
        hours += 1
    return f"{hours}:{minutes:02d}"

def main():
    cases = int(input())
    input()
    for i in range(cases):
        if i != 0:
            print()
        hangar = list(map(int, input().split()))
        total_edge_length = 0
        while True:       
            try:
                line = input()
                if line == "": break
            except EOFError:
                break

            source_x, source_y, dest_x, dest_y = list(map(int, line.split()))
            total_edge_length += edge_length((source_x, source_y), (dest_x, dest_y))

        time_in_seconds = total_edge_length*2/PLOW_SPEED_MPS
        print(f"{get_formatted_time_in_hours(time_in_seconds)}")


if __name__ == "__main__":
    main()