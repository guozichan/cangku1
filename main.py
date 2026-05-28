# # 导入所需库
# import tkinter as tk
# from tkinter import ttk, messagebox
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# # ====================== 修复 Matplotlib 中文显示 ======================
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# import warnings
# warnings.filterwarnings("ignore")  # 屏蔽无关警告
#
# # 计算挣值分析核心指标
# def calculate_eva():
#     try:
#         # 获取输入框数值
#         pv = float(entry_pv.get().strip())  # 计划值
#         ac = float(entry_ac.get().strip())  # 实际成本
#         ev = float(entry_ev.get().strip())  # 挣值
#
#         # 基础校验
#         if pv <= 0 or ac < 0 or ev < 0:
#             messagebox.showerror("输入错误", "计划值必须大于0，实际成本/挣值不能为负数！")
#             return
#
#         # 核心公式计算
#         cv = ev - ac       # 成本偏差
#         sv = ev - pv       # 进度偏差
#         cpi = ev / ac      # 成本绩效指数
#         spi = ev / pv      # 进度绩效指数
#
#         # 结果判断
#         cv_status = "成本节约" if cv > 0 else "成本超支" if cv < 0 else "成本持平"
#         sv_status = "进度提前" if sv > 0 else "进度滞后" if sv < 0 else "进度持平"
#         cpi_status = "低于预算" if cpi > 1 else "超出预算" if cpi < 1 else "按预算执行"
#         spi_status = "进度超前" if spi > 1 else "进度滞后" if spi < 1 else "按进度执行"
#
#         # 清空结果区域并展示数据
#         result_text.delete(1.0, tk.END)
#         result = f"""=== 挣值分析结果 ===
# 计划值 (PV)：{pv:.2f}
# 实际成本 (AC)：{ac:.2f}
# 挣值 (EV)：{ev:.2f}
#
# --- 偏差指标 ---
# 成本偏差 (CV) = EV - AC = {cv:.2f}  |  状态：{cv_status}
# 进度偏差 (SV) = EV - PV = {sv:.2f}  |  状态：{sv_status}
#
# --- 绩效指标 ---
# 成本绩效指数 (CPI) = EV/AC = {cpi:.2f}  |  状态：{cpi_status}
# 进度绩效指数 (SPI) = EV/PV = {spi:.2f}  |  状态：{spi_status}
# """
#         result_text.insert(tk.END, result)
#
#         # 绘制可视化图表
#         draw_chart(pv, ac, ev)
#
#     except ValueError:
#         messagebox.showerror("输入错误", "请输入有效的数字！")
#
# # 绘制挣值分析柱状图
# def draw_chart(pv, ac, ev):
#     # 清空画布
#     for widget in chart_frame.winfo_children():
#         widget.destroy()
#
#     # 创建图表
#     fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
#     labels = ['计划值(PV)', '实际成本(AC)', '挣值(EV)']
#     values = [pv, ac, ev]
#     colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
#
#     ax.bar(labels, values, color=colors)
#     ax.set_title('挣值分析对比图', fontsize=12)
#     ax.set_ylabel('金额/工作量', fontsize=10)
#     # 在柱子上显示数值
#     for i, v in enumerate(values):
#         ax.text(i, v + max(values)*0.02, f'{v:.2f}', ha='center', fontsize=9)
#
#     # 将图表嵌入GUI
#     canvas = FigureCanvasTkAgg(fig, master=chart_frame)
#     canvas.draw()
#     canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
#
# # 清空所有输入和结果
# def clear_all():
#     entry_pv.delete(0, tk.END)
#     entry_ac.delete(0, tk.END)
#     entry_ev.delete(0, tk.END)
#     result_text.delete(1.0, tk.END)
#     for widget in chart_frame.winfo_children():
#         widget.destroy()
#
# # ====================== GUI界面搭建 ======================
# root = tk.Tk()
# root.title("挣值分析(EVA)工具 - 简易版")
# root.geometry("900x600")  # 窗口大小
# root.resizable(False, False)
#
# # 顶部：输入区域
# input_frame = ttk.LabelFrame(root, text="项目数据输入")
# input_frame.place(x=20, y=20, width=860, height=120)
#
# ttk.Label(input_frame, text="计划值 (PV)：", font=("微软雅黑", 10)).grid(row=0, column=0, padx=15, pady=20)
# entry_pv = ttk.Entry(input_frame, width=15, font=("微软雅黑", 10))
# entry_pv.grid(row=0, column=1, padx=5)
#
# ttk.Label(input_frame, text="实际成本 (AC)：", font=("微软雅黑", 10)).grid(row=0, column=2, padx=15)
# entry_ac = ttk.Entry(input_frame, width=15, font=("微软雅黑", 10))
# entry_ac.grid(row=0, column=3, padx=5)
#
# ttk.Label(input_frame, text="挣值 (EV)：", font=("微软雅黑", 10)).grid(row=0, column=4, padx=15)
# entry_ev = ttk.Entry(input_frame, width=15, font=("微软雅黑", 10))
# entry_ev.grid(row=0, column=5, padx=5)
#
# # 按钮
# btn_calc = ttk.Button(input_frame, text="计算分析", command=calculate_eva)
# btn_calc.grid(row=0, column=6, padx=20)
#
# btn_clear = ttk.Button(input_frame, text="清空数据", command=clear_all)
# btn_clear.grid(row=0, column=7, padx=5)
#
# # 左侧：结果展示区域
# result_frame = ttk.LabelFrame(root, text="分析结果")
# result_frame.place(x=20, y=150, width=420, height=400)
#
# result_text = tk.Text(result_frame, font=("微软雅黑", 10), wrap=tk.WORD)
# result_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
#
# # 右侧：图表区域
# chart_frame = ttk.LabelFrame(root, text="可视化图表")
# chart_frame.place(x=460, y=150, width=420, height=400)
#
# # 主循环
# root.mainloop()
"""
挣值分析(EVA)可视化工具
符合 PEP8 编码规范 & GUI 最佳实践
功能：输入 PV/AC/EV，自动计算挣值指标并生成柱状图
"""
import tkinter as tk
from tkinter import ttk, messagebox

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import gc

# ====================== Matplotlib 全局配置 ======================
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('default')

# ====================== 全局常量（便于统一维护） ======================
WINDOW_TITLE = "挣值分析(EVA)工具 - 规范版"
WINDOW_SIZE = "900x600"
FONT_FAMILY = "微软雅黑"
FONT_SIZE = 10
DEFAULT_PV = 1000.0
DEFAULT_AC = 800.0
DEFAULT_EV = 900.0


class EVAAnalysisApp:
    """挣值分析主程序类，封装所有界面与逻辑"""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.resizable(False, False)

        # 绑定回车键快捷计算
        self.root.bind('<Return>', lambda event: self.calculate_eva())

        # 定义组件变量（避免全局变量）
        self.entry_pv = None
        self.entry_ac = None
        self.entry_ev = None
        self.result_text = None
        self.chart_frame = None

        # 初始化界面
        self._init_ui()

    def _init_ui(self):
        """初始化所有 UI 布局（私有方法）"""
        self._create_input_frame()
        self._create_main_content_frame()

    def _create_input_frame(self):
        """创建顶部输入区域"""
        input_frame = ttk.LabelFrame(self.root, text="项目数据输入")
        input_frame.pack(padx=20, pady=10, fill=tk.X)

        # 计划值 PV
        ttk.Label(input_frame, text="计划值 (PV)：", font=(FONT_FAMILY, FONT_SIZE)) \
            .grid(row=0, column=0, padx=15, pady=15)
        self.entry_pv = ttk.Entry(input_frame, width=15, font=(FONT_FAMILY, FONT_SIZE))
        self.entry_pv.grid(row=0, column=1, padx=5)
        self.entry_pv.insert(0, str(DEFAULT_PV))

        # 实际成本 AC
        ttk.Label(input_frame, text="实际成本 (AC)：", font=(FONT_FAMILY, FONT_SIZE)) \
            .grid(row=0, column=2, padx=15)
        self.entry_ac = ttk.Entry(input_frame, width=15, font=(FONT_FAMILY, FONT_SIZE))
        self.entry_ac.grid(row=0, column=3, padx=5)
        self.entry_ac.insert(0, str(DEFAULT_AC))

        # 挣值 EV
        ttk.Label(input_frame, text="挣值 (EV)：", font=(FONT_FAMILY, FONT_SIZE)) \
            .grid(row=0, column=4, padx=15)
        self.entry_ev = ttk.Entry(input_frame, width=15, font=(FONT_FAMILY, FONT_SIZE))
        self.entry_ev.grid(row=0, column=5, padx=5)
        self.entry_ev.insert(0, str(DEFAULT_EV))

        # 功能按钮
        ttk.Button(input_frame, text="计算分析", command=self.calculate_eva) \
            .grid(row=0, column=6, padx=20)
        ttk.Button(input_frame, text="清空数据", command=self.clear_all) \
            .grid(row=0, column=7, padx=5)

    def _create_main_content_frame(self):
        """创建结果 + 图表区域"""
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # 左侧结果区域
        result_frame = ttk.LabelFrame(main_frame, text="分析结果")
        result_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        self.result_text = tk.Text(result_frame, font=(FONT_FAMILY, FONT_SIZE), wrap=tk.WORD)
        self.result_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 右侧图表区域
        self.chart_frame = ttk.LabelFrame(main_frame, text="可视化图表")
        self.chart_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def calculate_eva(self):
        """执行挣值分析计算与结果展示"""
        try:
            # 1. 获取并校验输入
            pv_text = self.entry_pv.get().strip()
            ac_text = self.entry_ac.get().strip()
            ev_text = self.entry_ev.get().strip()

            if not all([pv_text, ac_text, ev_text]):
                messagebox.showwarning("输入提示", "请填写全部三项数据！")
                return

            pv = float(pv_text)
            ac = float(ac_text)
            ev = float(ev_text)

            # 2. 合法性校验
            if pv <= 0:
                messagebox.showerror("输入错误", "计划值(PV)必须大于 0")
                return
            if ac <= 0:
                messagebox.showerror("输入错误", "实际成本(AC)必须大于 0（避免除零错误）")
                return
            if ev < 0:
                messagebox.showerror("输入错误", "挣值(EV)不能为负数")
                return

            # 3. 核心公式计算
            cv = ev - ac
            sv = ev - pv
            cpi = ev / ac
            spi = ev / pv

            # 4. 完工预测指标（行业标准）
            etc = (pv - ev) / cpi if cpi != 0 else 0.0
            eac = ac + etc
            vac = pv - eac

            # 5. 状态文本
            cv_status = "✅ 成本节约" if cv > 0 else "❌ 成本超支" if cv < 0 else "⚪ 成本持平"
            sv_status = "✅ 进度提前" if sv > 0 else "❌ 进度滞后" if sv < 0 else "⚪ 进度持平"
            cpi_status = "✅ 低于预算" if cpi > 1 else "❌ 超出预算" if cpi < 1 else "⚪ 按预算执行"
            spi_status = "✅ 进度超前" if spi > 1 else "❌ 进度滞后" if spi < 1 else "⚪ 按进度执行"

            # 6. 展示结果
            self._show_result(pv, ac, ev, cv, sv, cpi, spi,
                              cv_status, sv_status, cpi_status, spi_status,
                              etc, eac, vac)

            # 7. 绘制图表
            self._draw_chart(pv, ac, ev)

        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的数字！")
        except Exception as e:
            messagebox.showerror("系统错误", f"程序异常：{str(e)}")

    def _show_result(self, pv, ac, ev, cv, sv, cpi, spi,
                      cv_status, sv_status, cpi_status, spi_status,
                      etc, eac, vac):
        """将计算结果格式化并显示到文本框"""
        result = f"""=== 挣值分析(EVA) 结果 ===
计划值 (PV)：{pv:.2f}
实际成本 (AC)：{ac:.2f}
挣值 (EV)：{ev:.2f}

--- 偏差指标 ---
成本偏差 (CV) = EV - AC = {cv:.2f}  |  {cv_status}
进度偏差 (SV) = EV - PV = {sv:.2f}  |  {sv_status}

--- 绩效指标 ---
成本绩效指数 (CPI) = EV/AC = {cpi:.2f}  |  {cpi_status}
进度绩效指数 (SPI) = EV/PV = {spi:.2f}  |  {spi_status}

--- 完工预测（标准EVA）---
完工尚需估算 (ETC)：{etc:.2f}
完工估算 (EAC)：{eac:.2f}
完工偏差 (VAC)：{vac:.2f}
"""
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def _draw_chart(self, pv: float, ac: float, ev: float):
        """绘制 PV/AC/EV 对比柱状图并嵌入界面"""
        # 清空旧组件
        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        # 关闭旧图表，防止内存泄漏
        plt.close('all')
        gc.collect()

        # 创建新图表
        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
        labels = ['计划值(PV)', '实际成本(AC)', '挣值(EV)']
        values = [pv, ac, ev]
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

        ax.bar(labels, values, color=colors)
        ax.set_title('挣值分析对比图', fontsize=12)
        ax.set_ylabel('数值', fontsize=10)

        # 柱子顶部显示数值
        max_val = max(values)
        for idx, val in enumerate(values):
            ax.text(idx, val + max_val * 0.02,
                   f'{val:.2f}', ha='center', fontsize=9)

        # 嵌入 Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def clear_all(self):
        """清空所有输入、结果与图表"""
        self.entry_pv.delete(0, tk.END)
        self.entry_ac.delete(0, tk.END)
        self.entry_ev.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)

        for widget in self.chart_frame.winfo_children():
            widget.destroy()

        plt.close('all')
        gc.collect()


def main():
    """程序主入口（标准规范写法）"""
    root = tk.Tk()
    app = EVAAnalysisApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()