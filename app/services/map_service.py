import pandas as pd
import folium

class Map_Service:
    @staticmethod
    def Find_Theater(lat, lng): 
        lotte = pd.read_csv("./app/static/lotte.csv")
        mega = pd.read_csv("./app/static/mega.csv")
        cgv = pd.read_csv("./app/static/cgv.csv")
        
        cinema_map = folium.Map(
            location=[lat, lng],  # 사용자의 현재 위치를 설정합니다.
            zoom_start=12,
            tiles='Stamen Terrain'
        )    
        # CSS 스타일을 사용하여 가운데 정렬된 HTML을 팝업 내용으로 설정
        def centered_popup_content(content):
            return f'<div style="text-align: center;">{content}</div>'

        # 롯데시네마 위치정보를 Marker로 표시
        for name, lat, lng in zip(lotte.지점, lotte.경도, lotte.위도):
            popup_content = centered_popup_content(name)
            folium.Marker(
                [lat, lng],
                popup=folium.Popup(popup_content, max_width=300),
                icon=folium.CustomIcon(icon_image="./app/static/lotte-modified.png",
            icon_size=(32, 32),)
            ).add_to(cinema_map)

        for name, lat, lng in zip(mega.지점, mega.경도, mega.위도):
            popup_content = centered_popup_content(name)
            folium.Marker(
                [lat, lng],
                popup=folium.Popup(popup_content, max_width=300),
                icon=folium.CustomIcon(icon_image="./app/static/mega-modified.png", icon_size=(32, 32))
            ).add_to(cinema_map)

            # cgv 위치정보를 CircleMarker로 표시
        for name, lat, lng in zip(cgv.지점, cgv.경도, cgv.위도):
            popup_content = centered_popup_content(name)
            folium.Marker(
                [lat, lng],
                popup=folium.Popup(popup_content, max_width=300),
                icon=folium.CustomIcon(icon_image="./app/static/cgv-modified.png", icon_size=(32, 32))
            ).add_to(cinema_map)

        cinema_map.save("./app/static/movie.html")
        cinema_map.save("./app/templates/movie.html")
        return True