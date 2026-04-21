# from game.sound.echo import *
# -> __all__과 상관없이 import된다.
# -> __all__ 설정 필요없다.

# from game.sound import *
# -> 는 모든 모듈
# -> __all__ 설정 필요하다.

from game.sound import *
# Initializing game ...

echo.echo_test() # echo

# sound밑에 __init__.py에 __all__을 안했을 경우
# Trackback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'echo' is not defined