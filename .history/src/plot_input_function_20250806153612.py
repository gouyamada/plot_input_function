"""
関数の入力文字列を受け取り、グラフを描画するスクリプト
"""
from typing import Any
import numpy as np
import numexpr as ne  # type: ignore
import matplotlib.pyplot as plt


def prepare_allowed_names(x: np.ndarray) -> dict[str, Any]:
    """ evalで使える名前空間を準備する関数 """
    return {
        # 変数
        "x": x,

        # 定数
        "pi": np.pi,
        "e": np.e,

        # 基本演算
        "abs": np.abs,
        "sqrt": np.sqrt,
        "power": np.power,

        # 指数・対数
        "exp": np.exp,
        "log": np.log,       # 自然対数
        "log10": np.log10,   # 常用対数
        "log2": np.log2,     # 底2の対数

        # 三角関数
        "sin": np.sin,
        "cos": np.cos,
        "tan": np.tan,
        "arcsin": np.arcsin,
        "arccos": np.arccos,
        "arctan": np.arctan,

        # 双曲線関数
        "sinh": np.sinh,
        "cosh": np.cosh,
        "tanh": np.tanh,
        "arcsinh": np.arcsinh,
        "arccosh": np.arccosh,
        "arctanh": np.arctanh,

        # その他の数学関数
        "floor": np.floor,
        "ceil": np.ceil,
        "round": np.round,
        "sign": np.sign,
        "clip": np.clip,
        "maximum": np.maximum,
        "minimum": np.minimum,
        "mod": np.mod,
        "remainder": np.remainder,

        # NumPyそのもの（任意で開放）
        "np": np,
    }


def evaluate_expression(expr: str, allowed_names: dict) -> np.ndarray | None:
    """ 入力式をexprを評価してyの値の配列を返す関数 """
    try:
        # numexprで安全に評価
        y = ne.evaluate(expr, local_dict=allowed_names)
        return y
    except (ValueError, SyntaxError, NameError) as e:
        print(f"エラーが発生しました: {e}")
        return None


def plot_function(x: np.ndarray, y: np.ndarray, expr: str):
    """ x, y の値で関数のグラフを描画する関数 """
    plt.rcParams["font.family"] = "Meiryo"
    plt.rcParams["font.size"] = 12
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
    """ 入力文字列をもとに関数を描画する関数 """
    x = np.linspace(x_range[0], x_range[1], num_points)
    allowed_names = prepare_allowed_names(x)
    y = evaluate_expression(expr, allowed_names)
    if y is not None:
        plot_function(x, y, expr)


def main():
    """ メイン関数 """
    expr = input("描画したい関数式を入力してください (例: sin(x) + x**2): ")
    plot_input_function(expr)


if __name__ == "__main__":
    main()
