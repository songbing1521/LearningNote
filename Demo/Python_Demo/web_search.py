import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time

def search_keyword(keyword, max_results=5):
    """
    搜索关键词并返回搜索结果
    
    参数:
    keyword (str): 要搜索的关键词
    max_results (int): 返回的最大结果数量
    
    返回:
    list: 包含(title, url)元组的列表
    """
    # 创建随机User-Agent
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    
    # 百度搜索URL
    url = f"https://www.baidu.com/s?wd={keyword}"
    
    try:
        # 发送请求（带超时设置）
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 检查HTTP错误
        
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        
        # 检查是否触发百度安全验证
        if soup.find('div', id='captcha'):
            print("触发百度安全验证，请稍后再试")
            return []
        
        # 新版百度搜索结果容器选择器
        result_containers = soup.select('.result-op, .c-container, .result')
        
        if not result_containers:
            print("未找到搜索结果容器，页面结构可能已更新")
            return []
        
        # 提取搜索结果
        for container in result_containers:
            # 标题选择器
            title_tag = container.find('h3') or container.find(class_='t')
            if not title_tag:
                continue
                
            # 链接选择器
            link_tag = title_tag.find('a') or container.find('a')
            if not link_tag or not link_tag.get('href'):
                continue
                
            title = title_tag.get_text().strip()
            link = link_tag['href']
            
            # 处理百度跳转链接
            if link.startswith('http'):
                results.append((title, link))
                
            # 达到最大结果数时停止
            if len(results) >= max_results:
                break
        
        return results
    
    except requests.exceptions.RequestException as e:
        print(f"搜索出错: {e}")
        return []
    except Exception as e:
        print(f"发生意外错误: {e}")
        return []

if __name__ == "__main__":
    keyword = input("请输入要搜索的关键词: ")
    print(f"正在搜索 '{keyword}'...")
    
    search_results = search_keyword(keyword)
    
    if search_results:
        print(f"\n找到 {len(search_results)} 条结果:")
        for i, (title, url) in enumerate(search_results, 1):
            print(f"{i}. {title}")
            print(f"   {url}\n")
    else:
        print("未找到相关结果")
