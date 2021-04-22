import React, { Component } from "react";
import { StyleSheet, View, Text, TouchableOpacity } from "react-native";
import Icon from "react-native-vector-icons/MaterialCommunityIcons";

function MaterialHeader1(props) {
  return (
    <View style={[styles.container, props.style]}>
      <View style={styles.textWrapper}>
        <Text numberOfLines={1} style={styles.piCctv}>
          Pi-cctv
        </Text>
      </View>
      <View style={styles.textWrapperFiller}></View>
      <TouchableOpacity style={styles.rightIconButton}>
        <Icon name="dots-vertical" style={styles.rightIcon}></Icon>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: "rgba(11,6,67,1)",
    flexDirection: "row",
    alignItems: "center",
    padding: 4,
    justifyContent: "space-between",
    shadowColor: "#111",
    shadowOffset: {
      width: 0,
      height: 2
    },
    shadowOpacity: 0.2,
    shadowRadius: 1.2,
    elevation: 3
  },
  textWrapper: {
    alignSelf: "flex-end",
    marginLeft: 72,
    marginBottom: 19
  },
  piCctv: {
    fontSize: 18,
    color: "#FFFFFF",
    backgroundColor: "transparent",
    lineHeight: 18
  },
  textWrapperFiller: {
    flex: 1,
    flexDirection: "row"
  },
  rightIconButton: {
    padding: 11,
    alignItems: "center",
    marginRight: 5,
    marginTop: 5
  },
  rightIcon: {
    backgroundColor: "transparent",
    color: "#FFFFFF",
    fontSize: 24
  }
});

export default MaterialHeader1;
