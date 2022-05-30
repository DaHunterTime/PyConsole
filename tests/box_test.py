from pyconsole import Box, GREEN, LIME, RESET


def box_test():
    box = Box("Normal box.\nNo color.\n:)")
    print(box)

    wide_box = Box("Same as above, but 'full screen' and border color",
                   full_screen=True, color=GREEN)
    print(wide_box)

    color_box = Box(f"{LIME}Success message{RESET}\n===============\nThat's it", color=GREEN)
    print(color_box)

    inside_box = Box(f"There is a box\n{Box(f'{LIME}SUCCESS{RESET}')}\ninside me", color=GREEN)
    print(inside_box)


if __name__ == "__main__":
    box_test()
