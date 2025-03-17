from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.image import Image as CoreImage
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.label import Label
from kivy.core.window import Window
import random
import os

# 配置窗口大小（适配手机竖屏）
Config.set('graphics', 'resizable', '0')
Window.size = (360, 640)  # 常见手机竖屏尺寸

# 游戏常量
GRID_SIZE = 20
CELL_SIZE = 25
INITIAL_SPEED = 0.15
DIRECTIONS = ['up', 'right', 'down', 'left']


class SnakeSegment:
    def __init__(self, pos):
        self.pos = pos


class Snake:
    def __init__(self):
        self.body = [SnakeSegment((GRID_SIZE // 2, GRID_SIZE // 2))]
        self.direction = 'right'
        self.growing = False

    @property
    def head(self):
        return self.body[0]

    def move(self):
        x, y = self.head.pos
        if self.direction == 'up':
            new_head = (x, y + 1)
        elif self.direction == 'down':
            new_head = (x, y - 1)
        elif self.direction == 'left':
            new_head = (x - 1, y)
        else:  # right
            new_head = (x + 1, y)

        self.body.insert(0, SnakeSegment(new_head))
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False

    def grow(self):
        self.growing = True


class Food:
    def __init__(self):
        self.pos = (0, 0)
        self.spawn()

    def spawn(self, snake_body=None):
        while True:
            self.pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            if snake_body is None or all(self.pos != seg.pos for seg in snake_body):
                break


class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.paused = False

        # 加载食物图片
        self.food_texture = None
        if os.path.exists("images/apple.png"):
            self.food_texture = CoreImage("images/apple.png").texture

        # 游戏计时器
        Clock.schedule_interval(self.update, INITIAL_SPEED)

        # 得分标签
        self.score_label = Label(
            text=f"Score: {self.score}",
            pos=(20, Window.height - 60),
            font_size='20sp'
        )
        self.add_widget(self.score_label)

    def on_touch_down(self, touch):
        if self.game_over:
            return
        # 触摸左半屏逆时针转，右半屏顺时针转
        if touch.x < self.width / 2:
            new_dir_index = (DIRECTIONS.index(self.snake.direction) - 1) % 4
        else:
            new_dir_index = (DIRECTIONS.index(self.snake.direction) + 1) % 4
        self.snake.direction = DIRECTIONS[new_dir_index]

    def update(self, dt):
        如果self.game_over或self.paused：
            返回

        self.snake.move（）

        ＃检测食物碰撞
        如果self.snake.head.pos == self.food.pos：
            self.score += 1
            self.score_label.text = f“得分：{self.score}”
            self.snake.grow（）
            self.food.spawn（[ （ seg.pos for for self self.snake.body ））

        ＃检测碰撞
        如果self.check_collision（）：
            self.game_over = true
            self.show_game_over（）

        self.draw（）

    def check_collision（self）：
        head = self.snake.head.pos
        ＃边界检测
        如果不是（0 <= head [  0  ] <grid_size和0<= head [  1  ] <grid_size）：
            返回true
        ＃自碰检测
        对于self.蛇。身体 [  1：]：
            如果头== seg.POS：
                返回是真的
        返回错误

    DEF SHOW_GAME_OVER（）：：：：：：：：：
        self.add_widget（标签（
            text = f“游戏
            pos =（self.Center_x- 100 ，自我。（center_y），
            font_size ='30sp' ，'30sp'，
            颜色= （1，0，0，1），，，，，，，，，，，
            粗体= true
        （（（））

    （def）（def）（def）（def）（（ def def def def def）：：：：
        self.canvas.clear（）
        与self.canvas：
            ＃绘制背景
            颜色（ 0.2，0.2，0.2）
            矩形（ pos =（0 （0），尺寸=窗口。窗口=，窗口。=，窗口。，窗口。，窗口。，窗口。，窗口。

            ＃绘制食物
            如果self.food_texture ::：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：：
                长方形（
                    纹理= self.food_texture，
                    pos = （（
                        self.food.pos [0] * cell_size +窗口。[0] * cell_size +窗口。
                        self.food.pos [1] * cell_size + 50 [1] * cell_size + 50
                    ），
                    尺寸=（cell_size，cell_size）
                （（（）
            别的：
                颜色（（（（（（（（（（1，0）
                长方形（
                    pos = （（
                        self.food.pos [0] * cell_size +窗口。[0] * cell_size +窗口。
                        self.food.pos [1 * cell_size + 50] * cell_size + 50
                    ），
                    尺寸=（cell_size，cell_size）
                （（（）

            ＃绘制蛇
            颜色（（（（（1，0）
            对于self.snake.body中的seg：
                长方形（
                    pos = （（
                        seg.pos [0 ] * cell_size +window.width -grid_size * cell_size cell_size） / 2，[ 0 ] * cell_size +cell_size +cell_size +cell_size +cell_size +window.width -grid_size * cell_size * cell_size * cell_size * cell_size * cell_size * cell_size * cell_size * cell_size * cell_size * cell_size）
                        seg.pos [1] * cell_size + 50 [1] * cell_size + 50
                    ），
                    size =（cell_size -1，cell_size -1）
                （（（）


（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（ Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）snakeapp）（Snakeapp）（Snakeapp）snakeapp）（Snakeapp）Snakeapp）Snakea （snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）snakeapp）（snakeapp）snakeapp）（snakeapp）snakeapp）（snakeapp）（snakeapp）snakeapp）（sn （Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（snakeapp）（Snakeapp）（snakeapp）（snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）Snakeapp）（Snakeapp）） （snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（Snakeapp）（snakeapp）（Snakeapp））（snakeapp）（snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（（（（（））（（（（））（（（））（（））（））（）（蛇） （snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（Snakeapp）（Snakeapp）（snakeapp）（Snakeapp）（Snakeapp）（Snakeapp））（Snakeapp）） （snakeapp）（snakeapp）（snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（snakeapp）（Snakeapp）snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）Snakeapp）（Snakeapp）Snakeapp）Snakeapp）snakeapp）snak）（ （（Snakeapp））（sn （akeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）snakeapp）（snakeapp）（snakeapp）（snakeapp）（（Snakeapp）（snakeapp）（ （Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）Snakeapp）Sn （snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）snakeapp）（Snakeapp）（snakeapp）snakeapp）snakeapp）（snake）（蛇（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp）（Snakeapp））（Snakeapp））
    Def Build （自我）：
        game = snakegame（）
        ＃游戏区域居中显示
        game.pos = 50 （50）（50）（50）（50）50）（50）（50）（50）（50）（50）（50）（50）50）（50）（50）（50）50）50）（50）50）50）50）50）（50）50）（50）50）（50）50）（50）50）50）50）50）50）50）50）50）50）50）50）50）50）50）50）（50 ）（50）（50）50）（50）50）（50）（50）50）50）50）50）50）50）50）50）50））50）50））50）50））50））50））50））
        返回游戏


如果__- ____ =='__-主要__ __':::::::::::::::::::::::：:::::::::::::::::: :::::::::: ::::::: ::::: :::: ___-'____- _________
    （snakeapp）（（（（snakeapp）））
