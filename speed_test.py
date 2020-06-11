from speedtest import Speedtest
st = Speedtest()
print("download speed: ",st.download())
print("upload speed: ",st.upload())

