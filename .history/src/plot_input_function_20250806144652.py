"""
関数の入力文字列を受け取り、グラフを描画するスクリプト
"""
import numpy as np
import matplotlib.pyplot as plt


def prepare_allowed_names(x: str) -> dict:
    """ evalで使える名前空間を準備する関数 """
    return {
        "x": x,
        "np": np,
        "sin": np.sin,
        "cos": np.cos,
        "tan": np.tan,
        "exp": np.exp,
        "log": np.log,
        "sqrt": np.sqrt,
        "abs": np.abs,
        "pi": np.pi,
        "e": np.e,
    }


def evaluate_expression(expr: str, x, allowed_names):
    """ 入力式を評価して y を返しますの """
    try:
        y = eval(expr, {"__builtins__": {}}, allowed_names)
        return y
    except Exception as e:
        print(f"エラーが発生いたしましたわ: {e}")
        return None


def plot_function(x: float, y: float, expr):
    """ x, y の値で関数のグラフを描画いたしますの """
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=expr, color='blue')
    plt.title(f"関数のグラフ: {expr}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_input_function(expr: str, x_range=(-10, 10), num_points=400):
    """ 入力文字列をもとに関数を描画いたしますの（統括） """
    x = np.linspace(x_range[0], x_range[1], num_points)
    allowed_names = prepare_allowed_names(x)
    y = evaluate_expression(expr, x, allowed_names)
    if y is not None:
        plot_function(x, y, expr)


def main():
    """ メイン関数 """
    expr = input("描画したい関数式を入力してくださいませ（例: sin(x) + x**2）: ")
    plot_input_function(expr)


if __name__ == "__main__":
    main()
