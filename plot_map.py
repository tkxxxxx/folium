# -*- coding: utf-8 -
import folium


def main():

    # 東京都港区芝公園を設定
    haneda_location = [35.5554, 139.7544]
    # 地図の基準として羽田空港を設定
    # 基準地点にマーカーを設置する

    m = folium.Map(location=haneda_location,
                   #attr='OpenStreetMap',
                   attr='stamenterrain',
                   zoom_start=11)
    geojson = r'tokyo23.json'
    # geojson読み込み
    m.choropleth(geo_data=geojson)
    folium.Marker(haneda_location, popup='Haneda').add_to(m)
    # 地図をhtml形式で出力
    m.save(outfile="map.html")

if __name__ == "__main__":
    main()
