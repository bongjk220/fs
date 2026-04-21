# 전체 경로
#from game.sound.echo import echo_test

# 상대 경로
from ..sound.echo import echo_test

def render_test():
    print("render가 잘 호출되었네요.")
    echo_test() # echo