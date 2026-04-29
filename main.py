import logging
from datetime import datetime
from agents.listing_agent import generate_listing
from agents.pricing_agent import suggest_price
from agents.chat_agent import auto_reply
from db import init_db, save_product, get_all_products

# =========================
# 日志配置（很加分）
# =========================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# =========================
# 核心流程（Orchestrator）
# =========================
def run_pipeline(user_input: str):
    logger.info("Starting pipeline...")

    try:
        # 1️⃣ 文案生成
        logger.info("Calling Listing Agent...")
        listing = generate_listing(user_input)

        # 2️⃣ 定价
        logger.info("Calling Pricing Agent...")
        price = suggest_price(user_input)

        product = {
            "title": listing.get("title"),
            "desc": listing.get("desc"),
            "price": price,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # 3️⃣ 存储
        save_product(product)
        logger.info("Product saved to database")

        # 4️⃣ 输出结果
        print("\n====== 生成结果 ======")
        print(f"标题: {product['title']}")
        print(f"描述: {product['desc']}")
        print(f"价格: ¥{product['price']}")
        print("=====================\n")

        return product

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        return None


# =========================
# 模拟聊天（展示 Agent 感）
# =========================
def simulate_chat():
    print("\n进入自动回复模式（输入 exit 退出）")

    while True:
        user_msg = input("买家：")
        if user_msg.lower() == "exit":
            break

        reply = auto_reply(user_msg)
        print(f"AI：{reply}")


# =========================
# CLI 入口（真实项目常见）
# =========================
def main():
    init_db()

    print("=== 二手交易 AI 助手 ===")
    print("1. 发布商品")
    print("2. 查看商品")
    print("3. 模拟聊天")
    print("0. 退出")

    while True:
        choice = input("\n请选择操作：")

        if choice == "1":
            user_input = input("请输入商品描述：")
            run_pipeline(user_input)

        elif choice == "2":
            products = get_all_products()
            print("\n=== 商品列表 ===")
            for p in products:
                print(f"{p['id']} | {p['title']} | ¥{p['price']}")
            print("================")

        elif choice == "3":
            simulate_chat()

        elif choice == "0":
            print("退出程序")
            break

        else:
            print("无效选项，请重新输入")


# =========================
# 程序入口
# =========================
if __name__ == "__main__":
    main()