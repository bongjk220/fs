# 방법1
'''
    import 패키지명.모듈명
'''
import game.sound.echo
game.sound.echo.echo_test()  # echo

# 방법2
'''
    from 패키지명 import 모듈명
'''
from game.sound import echo
echo.echo_test() # echo

# 방법3
'''
    from 패키지명.모듈명 import 함수명
'''
from game.sound.echo import echo_test
echo_test() # echo

