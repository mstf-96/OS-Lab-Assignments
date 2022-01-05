import arcade

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 160
BOTTOM_MARGIN = 160

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Complex Loops - Box")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for row in range(10):
    for column in range(10):
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        if (row+1) % 2 == 0:
            if (column+1) % 2 != 0:
                print(column)
                arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.BLUE, 45)

            else:
                arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.RED, 45)

        else:
            if (column + 1) % 2 != 0:
                arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.RED, 45)

            else:
                arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.BLUE, 45)

arcade.finish_render()

arcade.run()