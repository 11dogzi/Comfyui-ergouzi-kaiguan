![灵仙儿和二狗子](docs/LOGO2.png "LOGO2")
哈喽！我是二狗子（2🐕）！这是一套针对Comfyui流程设计师及玩家的混合组开关套件，一键实现控制不同组别的忽略禁用   
Hello! I am Er Gouzi （2🐕）！ This is a mixed group switch kit designed for Comfyui process designers and players, which allows for one click control of ignoring and disabling different groups

## 安装
Installation

首先，打开命令行终端，然后切换到您的ComfyUI的`custom_nodes`目录：   
Firstly, open the command line terminal and then switch to the 'custom_dodes' directory in your ComfyUI:   

```cd /path/to/your/ComfyUI/custom_nodes```

将/path/to/your/ComfyUI替换为您的ComfyUI项目所在的实际路径。   
Replace/path/to/your/ComfyUI with the actual path where your ComfyUI project is located.   
接下来，克隆ergouzi-kaiguan仓库：   
Next, clone the ergouzi kaiguan repository:   

```git clone https://github.com/11dogzi/Comfyui-ergouzi-kaiguan.git```

## 视频使用教程    
Video usage tutorial    
[视频使用教程][开关节点使用视频教程](https://www.bilibili.com/video/BV1bT421677t/?vd_source=ab266c754171024c866a35bf8097094e)      

## 节点介绍
Node Introduction
## 通用开关节点："Universal switch▶️"    
通过节点右键菜单选项卡进行开关设置，对全局的节点组进行开关方案的勾选，多个"Universal switch▶️"节点建立时，将会每次仅打开的节点生效，防止开关冲突   
Set the switch through the right-click menu tab of the node, select the switch scheme for the global node group, and use multiple"Universal switch▶️"options When a node is established, only the opened nodes will take effect each time to prevent switch conflicts    
![灵仙儿和二狗子](docs/全局开关.png "全局开关")    
![灵仙儿和二狗子](docs/全局开关1.png "全局开关1")    

## 连线开关节点："All Ignore👁️‍🗨️▶️"    
当该节点连接"ALL🚫👁️‍🗨️"时，则对当前节点连接的"ALL🚫👁️‍🗨️"所在组进行忽略处理，可连接多个"ALL🚫👁️‍🗨️"控制多组    
When the node is connected to"ALL🚫👁️‍🗨️"When, the"ALL🚫👁️‍🗨️"connected to the current node"ALL🚫👁️‍🗨️"Ignore the group and connect multiple"ALL🚫👁️‍🗨️"Control multiple groups    
![灵仙儿和二狗子](docs/连线忽略.png "连线忽略")       

## 连线开关节点："All Disable🚫"    
当该节点连接"ALL🚫👁️‍🗨️"时，则对当前节点连接的"ALL🚫👁️‍🗨️"所在组进行禁用处理，可连接多个"ALL🚫👁️‍🗨️"控制多组    
When the node is connected to"ALL🚫👁️‍🗨️"When, the"ALL🚫👁️‍🗨️"connected to the current node"ALL🚫👁️‍🗨️"Disable the group to which you belong, multiple"ALL🚫👁️‍🗨️"connections can be made"ALL🚫👁️‍🗨️"Control multiple groups    
![灵仙儿和二狗子](docs/连线禁用.png "连线禁用")    

## 连线混合开关节点："Hybrid switch🔃"    
当该节点连接"hulue🔃"时，则对当前节点连接的"hulue🔃"所在组进行忽略处理，当该节点连接"jin yong🔃"时，则对当前节点连接的"jin yong🔃"所在组进行禁用处理，可连接多个"jin yong🔃"或者"hulue🔃"进行混合控制    
When the node is connected to"hulue🔃"，The "hulue🔃" of the current node connection Ignore the group you belong to，When the node connects to"jin yong🔃"，The"jin yong🔃"connected to the current node Disable the group in which it belongs，Can connect multiple "jin yong🔃" Or "hulue🔃" Perform mixed control
![灵仙儿和二狗子](docs/连线混合.png "连线混合")     

## 开关点示例： 
Example of switch points    
![灵仙儿和二狗子](docs/开关点.png "开关点")   

## 开关名称设置：    
Switch name setting    
![灵仙儿和二狗子](docs/连线式开关.png "连线式开关")    
![灵仙儿和二狗子](docs/开关名称修改.png "开关名称修改")    

## 功能节点："Recursive switching🔀"    
输入N个输入，对第一个非空值进行输出，可以设置需要切换的输入数量以及记录每个输入点名称    
Input N inputs and output the first non null value. You can set the number of inputs to switch and record the name of each input point
![灵仙儿和二狗子](docs/任意切换.png "任意切换")    
![灵仙儿和二狗子](docs/任意切换1.png "任意切换1")    
![灵仙儿和二狗子](docs/任意切换3.png "任意切换3")    


## 更多SD免费教程
More SD free tutorials   
灵仙儿和二狗子的Bilibili空间，欢迎访问：   
Bilibili space for Lingxian'er and Ergouzi, welcome to visit:   
[灵仙儿二狗子的Bilibili空间](https://space.bilibili.com/19723588?spm_id_from=333.1007.0.0)   
欢迎加入我们的QQ频道，点击这里进入：   
Welcome to our QQ channel, click here to enter:   
[二狗子的QQ频道](https://pd.qq.com/s/3d9ys5wpr)   
![LOGO](docs/LOGO1.png "LOGO1")![LOGO](docs/LOGO1.png "LOGO1")![LOGO](docs/LOGO1.png "LOGO1") 


















