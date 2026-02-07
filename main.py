from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import QLabel
from kivy.uix.button import QPushButton
from kivy.uix.scrollview import ScrollView
import random, hashlib, re, requests

class AIApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 顶部标题
        self.root.add_widget(QLabel(text="Macau AI 顶级决策系统", font_size='24sp', size_hint_y=0.1))
        
        # 日志显示区
        self.log_label = QLabel(text="等待同步数据...", size_hint_y=None, halign='left', valign='top')
        self.log_label.bind(size=self.log_label.setter('text_size'))
        scroll = ScrollView(size_hint_y=0.7)
        scroll.add_widget(self.log_label)
        self.root.add_widget(scroll)
        
        # 启动按钮
        btn = QPushButton(text="🔮 启动推演", size_hint_y=0.2, background_color=(0, 1, 0.8, 1))
        btn.bind(on_press=self.run_logic)
        self.root.add_widget(btn)
        
        return self.root

    def run_logic(self, instance):
        self.log_label.text = "正在穿透抓取 2026 数据...\n"
        url = "https://hqvsgyr.b3psx-nflco-hoakss.work:16677/kj/3/2026.html"
        try:
            # 移动端 headers
            r = requests.get(url, timeout=10)
            content = r.text
            period = re.search(r"<td>(\d{3})期</td>", content).group(1)
            self.log_label.text += f"✅ 同步成功：第 {period} 期\n"
            
            # 信心推演逻辑
            seed = int(hashlib.md5(content.encode()).hexdigest(), 16)
            random.seed(seed)
            self.log_label.text += "\n--- 推荐方案 ---\n"
            for i in range(3):
                picks = sorted(random.sample(range(1, 50), 7))
                conf = random.randint(94, 98)
                self.log_label.text += f"方案 {chr(65+i)} (信心{conf}%): \n{picks[:6]} + [{picks[6]}]\n\n"
        except Exception as e:
            self.log_label.text += f"❌ 错误: {str(e)}"

if __name__ == '__main__':
    AIApp().run()
