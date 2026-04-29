import time
import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# ================================
# Logger
# ================================

class Logger:
    def __init__(self):
        self.logs = []

    def log(self, agent, message, level="INFO"):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{now}] [{level}] [{agent}] {message}"
        print(line)
        self.logs.append(line)

    def delay(self, min_s=0.1, max_s=0.5):
        time.sleep(random.uniform(min_s, max_s))


# ================================
# Listing Agent（高密度）
# ================================

def listing_agent(logger):
    logger.log("ListingAgent", "Start processing listing task")
    logger.log("ListingAgent", "Parsing input data...")
    logger.delay()

    logger.log("ListingAgent", "Extracting image features...")
    for i in range(random.randint(2, 5)):
        logger.delay()
        logger.log("ListingAgent", f"Image {i+1} feature extracted")

    logger.log("ListingAgent", "Analyzing product condition...")
    logger.delay()

    titles = [
        "95新 iPhone13 无拆修",
        "自用 iPhone13 成色很好",
        "急出 iPhone13 支持验机"
    ]

    for i in range(3):
        logger.delay()
        logger.log("ListingAgent", f"Generating candidate title {i+1}")

    title = random.choice(titles)
    logger.log("ListingAgent", f"Selected title: {title}")

    logger.log("ListingAgent", "Generating description...")
    logger.delay()
    logger.log("ListingAgent", "Description optimized")

    logger.log("ListingAgent", "Listing generation completed")


# ================================
# Pricing Agent（高密度）
# ================================

def pricing_agent(logger):
    logger.log("PricingAgent", "Start price analysis")
    logger.log("PricingAgent", "Querying market data...")
    logger.delay()

    prices = []
    for i in range(random.randint(5, 10)):
        price = random.randint(1100, 1500)
        prices.append(price)
        logger.delay()
        logger.log("PricingAgent", f"Fetched price sample: {price}")

    logger.log("PricingAgent", "Cleaning outliers...")
    logger.delay()

    logger.log("PricingAgent", "Calculating average price...")
    suggested = int(sum(prices) / len(prices))
    min_price = suggested - random.randint(50, 100)

    logger.log("PricingAgent", f"Suggested price: {suggested}")
    logger.log("PricingAgent", f"Minimum price: {min_price}")

    logger.log("PricingAgent", "Price analysis completed")

    return suggested, min_price


# ================================
# Posting Agent（高密度）
# ================================

def posting_agent(logger):
    logger.log("PostingAgent", "Initializing browser session")
    logger.delay()

    logger.log("PostingAgent", "Loading user cookies...")
    logger.delay()

    logger.log("PostingAgent", "Opening publish page...")
    logger.delay()

    logger.log("PostingAgent", "Uploading images...")
    for i in range(random.randint(3, 6)):
        logger.delay()
        logger.log("PostingAgent", f"Uploading image {i+1}")

    if random.random() < 0.3:
        logger.log("PostingAgent", "Upload failed, retrying...", "ERROR")
        logger.delay()
        logger.log("PostingAgent", "Retry success")

    logger.log("PostingAgent", "Filling title...")
    logger.delay()

    logger.log("PostingAgent", "Filling description...")
    logger.delay()

    logger.log("PostingAgent", "Submitting form...")
    logger.delay()

    logger.log("SYSTEM", "Item posted successfully", "SUCCESS")


# ================================
# Chat Agent（高密度）
# ================================

def chat_agent(logger, min_price):
    logger.log("ChatAgent", "Initializing message listener")
    logger.delay()

    for _ in range(random.randint(2, 4)):
        logger.log("ChatAgent", "Polling message queue...")
        logger.delay()

    messages = ["在吗", "可以便宜吗", "包邮吗", "最低多少"]
    msg = random.choice(messages)

    logger.log("ChatAgent", f"Incoming message: {msg}")
    logger.log("ChatAgent", "Analyzing intent...")
    logger.delay()

    if "便宜" in msg or "最低" in msg:
        logger.log("NegotiationAgent", "Entering negotiation mode")
        logger.delay()

        for i in range(2):
            logger.log("NegotiationAgent", f"Evaluating offer round {i+1}")
            logger.delay()

        offer = min_price + random.randint(0, 80)
        logger.log("NegotiationAgent", f"Counter offer: {offer}")

    elif "包邮" in msg:
        logger.log("ChatAgent", "Matched FAQ: shipping")
        logger.log("ChatAgent", "Reply: 可以包邮")

    else:
        logger.log("ChatAgent", "Default reply triggered")
        logger.log("ChatAgent", "Reply: 在的，可以直接拍")


# ================================
# Orchestrator（系统级日志）
# ================================

def run_pipeline():
    logger = Logger()

    task_id = random.randint(1000, 9999)

    logger.log("SYSTEM", f"Task created: {task_id}")
    logger.log("SYSTEM", "Initializing agents...")
    logger.delay()

    logger.log("SYSTEM", "Dispatching to ListingAgent")
    listing_agent(logger)

    logger.log("SYSTEM", "Dispatching to PricingAgent")
    suggested, min_price = pricing_agent(logger)

    logger.log("SYSTEM", "Dispatching to PostingAgent")
    posting_agent(logger)

    logger.log("SYSTEM", "Dispatching to ChatAgent")
    chat_agent(logger, min_price)

    logger.log("SYSTEM", f"Task {task_id} completed")

    return logger.logs


# ================================
# 保存日志
# ================================

def save_log(logs, filename="run.log"):
    with open(filename, "w", encoding="utf-8") as f:
        for line in logs:
            f.write(line + "\n")


# ================================
# 生成终端截图
# ================================

def generate_image(logs):
    img = Image.new("RGB", (1200, 800), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    y = 10
    for line in logs:
        draw.text((10, y), line, fill=(0, 255, 0))
        y += 18
        if y > 780:
            break

    img.save("terminal.png")


# ================================
# main
# ================================

if __name__ == "__main__":
    logs = run_pipeline()
    save_log(logs)
    generate_image(logs)

    print("\n生成完成：run.log + terminal.png")