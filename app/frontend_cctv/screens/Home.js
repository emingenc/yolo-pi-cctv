import React, { Component , useEffect, useState} from "react";
import { StyleSheet, View, Image, Text } from "react-native";
import MaterialHeader1 from "../components/MaterialHeader1";
import axios from 'axios';

function Home(props) {

  const [images,setImages]=useState([]);
  let callFreq = 10000

  setInterval( () => {
    axios.get(`http://192.168.1.25:8000/latest`)
    .then(res => {
      const images = res.data;
      console.log(images)
      setImages(images);
    })
  }, callFreq); //api call in every x seconds

  let latestImage = ''
  let latestImageDeviceName = ''
  let latestImageFrameNo = ''
  let latestImageTime = ''
  if (images.length > 0){
    latestImage = images[0].image
    latestImageDeviceName = images[0].device_name
    latestImageFrameNo = images[0].frame
    latestImageTime = images[0].time
  }
  return (
    <View style={styles.container}>
      <View style={styles.groupStackStack}>
        <View style={styles.groupStack}>
          <View style={styles.group}>
            <Image
              source={`data:image/jpeg;base64,${latestImage}`}
              resizeMode="contain"
              style={styles.imageDetail}
            ></Image>
          </View>
          <View style={styles.group2}>
            <View style={styles.infosFiller}></View>
            <View style={styles.infos}>
              <View style={styles.rectFiller}></View>
              <View style={styles.rect}>
                <Text style={styles.frameNumber}>Frame number:{latestImageFrameNo}</Text>
                <Text style={styles.deviceName}>Device name:{latestImageDeviceName}</Text>
                <Text style={styles.time}>Time:{latestImageTime}</Text>
              </View>
            </View>
          </View>
        </View>
        <View style={styles.bottomimages}>
          <View style={styles.bottomimagebg}></View>
  
           {images.map(image => {
              return(
                <Image
                source={`data:image/jpeg;base64,${image.image}`}
                resizeMode="cover"
                style={styles.image2}
              ></Image>
              )
            })}
        </View>
      </View>
      <MaterialHeader1 style={styles.materialHeader1}></MaterialHeader1>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "rgba(4,2,28,1)"
  },
  group: {
    width: 980,
    height: 690,
    position: "absolute",
    left: 0,
    top: 12
  },
  imageDetail: {
    width: 886,
    height: 589,
    marginTop: 25,
    marginLeft: 32
  },
  group2: {
    top: 0,
    height: 809,
    position: "absolute",
    right: 0,
    width: 612,
    flexDirection: "row"
  },
  infosFiller: {
    flex: 1,
    flexDirection: "row"
  },
  infos: {
    width: 435,
    height: 626,
    backgroundColor: "rgba(58,52,169,0.56)",
    borderRadius: 25,
    flexDirection: "row",
    marginRight: 40,
    marginTop: 17
  },
  rectFiller: {
    flex: 1,
    flexDirection: "row"
  },
  rect: {
    width: 408,
    height: 591,
    backgroundColor: "rgba(77,70,198,0.25)",
    borderRadius: 25,
    alignItems: "flex-end",
    marginRight: 10,
    marginTop: 16
  },
  frameNumber: {
    fontFamily: "roboto-700",
    color: "rgba(255,255,255,1)",
    width: 304,
    lineHeight: 14,
    fontSize: 21,
    height: 29,
    marginTop: 171,
    marginRight: 80
  },
  deviceName: {
    fontFamily: "roboto-700",
    color: "rgba(255,255,255,1)",
    width: 304,
    lineHeight: 14,
    fontSize: 21,
    height: 66,
    marginTop: 78,
    marginRight: 80
  },
  time: {
    fontFamily: "roboto-700",
    color: "rgba(255,255,255,1)",
    width: 277,
    lineHeight: 14,
    fontSize: 21,
    height: 61,
    marginTop: 52,
    marginRight: 107
  },
  groupStack: {
    top: 0,
    left: 36,
    width: 1547,
    height: 809,
    position: "absolute"
  },
  bottomimages: {
    left: 0,
    width: 1606,
    position: "absolute",
    flexDirection: "row",
    justifyContent: "space-around",
    bottom: 0,
    height: 105
  },
  bottomimagebg: {
    left: 0,
    position: "absolute",
    backgroundColor: "rgba(58,52,169,1)",
    opacity: 0.56,
    width: 1620,
    bottom: -27,
    height: 160
  },
  image2: {
    width: 108,
    height: 105
  },
  groupStackStack: {
    width: 1606,
    height: 840,
    marginTop: 111,
    marginLeft: 138
  },
  materialHeader1: {
    height: 77,
    marginTop: -951
  }
});

export default Home;
