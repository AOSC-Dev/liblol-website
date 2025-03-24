# coding=utf-8
import json
import pandas as pd
import requests


def get_last_info():
    url = "http://113.24.212.22:8080/community/app/latests"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0"
                      "Safari/537.36 Edg/120.0.0.0",
    }
    data = {
        "page": 1,
        "per_page": 1
    }
    res = requests.post(url, headers=headers, json=data)
    dict = json.loads(res.text)
    dict = dict["data"]
    total = dict["total"]
    dict = dict["vodata"]
    last_app_info = pd.DataFrame(dict)
    return last_app_info, total, res.text


def get_all_info():
    # 获取所有app的信息，开发者信息和app详情页地址需另行获取
    url = "http://113.24.212.22:8080/community/app/latests"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0"
                      "Safari/537.36 Edg/120.0.0.0",
    }
    data = {
        "page": 1,
        "per_page": get_last_info()[1]
    }
    res = requests.post(url, headers=headers, json=data)
    dict = json.loads(res.text)
    dict = dict["data"]
    dict = dict["vodata"]
    df_info = pd.DataFrame(dict)
    # 获取开发者信息 & app详情页地址
    url_first = "http://app.loongapps.cn/detail/"
    url_list = []
    dev_list = []
    for app_id in df_info["id"]:
        url = "http://113.24.212.22:8080/community/app"
        data = {"process": "INFO", "id": app_id}
        res = requests.post(url, headers=headers, json=data,stream= False,timeout= 10)
        dict = json.loads(res.text)
        res.keep_alive = False
        dict = dict["data"]
        app_url = url_first + str(app_id)
        url_list.append(app_url)
        dev_list.append(dict["developerName"])
    df_dev_list = pd.DataFrame(dev_list)
    df_url_list = pd.DataFrame(url_list)
    # 构造完整信息
    df_info["developerName"] = df_dev_list
    df_info["appUrl"] = df_url_list
    data = []
    df_data = pd.DataFrame(data)
    df_data["应用编号"] = df_info["id"]
    df_data["应用名称"] = df_info["name"]
    df_data["页面链接"] = df_info["appUrl"]
    df_data["版本号"] = df_info["version"]
    df_data["下载链接"] = df_info["downloadUrl"]
    df_data["文件大小"] = df_info["appSize"]
    df_data["应用类型"] = df_info["categoryName"]
    df_data["开发者"] = df_info["developerName"]
    df_data["更新时间"] = df_info["updateTime"]
    df_data["图片链接"] = df_info["logoUrl"]
    df_data["可执行文件"] = df_info["exec"]
    return df_data

def main():
    df_new = pd.DataFrame(
        columns=["应用编号", "应用名称", "页面链接", "版本号", "下载链接", "文件大小", "应用类型", "开发者", "更新时间",
                 "图片链接", "可执行文件"])
    df_down = df_upgrade = df_update = df_new
    df_get = get_all_info()
    df_latest = pd.read_csv("loongapplist-latest.csv", encoding="utf-8-sig")
    if str(df_get["应用编号"]) == str(df_latest["应用编号"])  and str(df_get["版本号"]) == str(df_latest["版本号"]) :
        print("无更新")
    else:
        for id in df_get["应用编号"]:
            if id in df_latest["应用编号"].values and df_latest.loc[df_latest["应用编号"] == id, "版本号"].values[0] == \
                    df_get.loc[df_get["应用编号"] == id, "版本号"].values[0]:
                print(str(id) + "未更新")
            elif id in df_latest["应用编号"].values and df_latest.loc[df_latest["应用编号"] == id, "版本号"].values[
                0] != \
                    df_get.loc[df_get["应用编号"] == id, "版本号"].values[0]:
                print(str(id) + "有新版本")
                df_upgrade = df_upgrade._append(df_get.loc[df_get["应用编号"] == id], ignore_index=True)
            elif id not in df_latest["应用编号"].values:
                print(str(id) + "是新应用")
                df_new = df_new._append(df_get.loc[df_get["应用编号"] == id], ignore_index=True)
        for id in df_latest["应用编号"]:
            if id not in df_get["应用编号"].values:
                print(str(id) + "已下架")
                df_down = df_down._append(df_latest.loc[df_latest["应用编号"] == id], ignore_index=True)
        df_update = df_update._append(df_new, ignore_index=True)
        df_update = df_update._append(df_down, ignore_index=True)
        df_update = df_update._append(df_upgrade, ignore_index=True)
        for name in df_update["应用名称"]:
            a = "3A4000"
            if a in name:
                df_update.drop((df_update[df_update["应用名称"] == name]).index, inplace=True)
            else:
                continue
        df_update.drop(columns="图片链接", axis=1, inplace=True)
        df_update.sort_values("应用编号", ascending=True, inplace=True)
        # 删除开源软件
        df_update.drop((df_update[df_update["开发者"] == "开源软件"]).index, inplace=True)
        # 删除二进制翻译软件
        df_update.drop((df_update[df_update["开发者"] == "二进制翻译软件"]).index, inplace=True)
        # 删除开源软件（云顶书院迁移）
        df_update.drop((df_update[df_update["开发者"] == "开源软件（云顶书院迁移）"]).index, inplace=True)
        df_update.rename(
            columns={
                "应用编号": "编号",
                # "安装教程": "详细信息",
                "版本号": "版本",
            },
            inplace=True,
        )
        df_down.to_csv("loongapplist-down.csv", encoding="utf-8-sig", index=False)
        df_new.to_csv("loongapplist-new.csv", encoding="utf-8-sig", index=False)
        df_upgrade.to_csv("loongapplist-upgrade.csv", encoding="utf-8-sig", index=False)
        df_get.to_csv("loongapplist-latest.csv", encoding="utf-8-sig", index=False)
        df_update.to_csv("loongapplist-update.csv", encoding="utf-8-sig", index=False)


if __name__ == '__main__':
    main()
