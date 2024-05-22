import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  container: {
    flex: 1,
    display: "flex",
    flexDirection: "column",
    width: "100%",
    height: "100%",
    backgroundColor: "#339dd7",
    position: "relative",
  },
  boxBackgroundTop: {
    width: "100%",
    height: "30%",
    backgroundColor: "#339dd7",
    borderBottomEndRadius: 35,
    borderBottomStartRadius: 35,
  },
  textMenu: {
    color: "#fff",
    marginTop: 80,
    fontWeight: "500",
    alignSelf: "center",
    fontSize: 40,
  },
  main: {
    width: "85%",
    height: "70%",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    top: 170,
    position: "absolute",
    bottom: 200,
    alignSelf: "center",
    borderRadius: 35,
    backgroundColor: "#339dd7",
  },
  boxLine: {
    width: "100%",
    height: "30%",
    flexDirection: "row",
    justifyContent: "space-around",
  },
  boxOption: {
    width: "45%",
    height: "100%",
    borderRadius: 20,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#fff",
  },
  textOption: {
    color: "#339dd7",
    fontSize: 20,
    fontWeight: "bold",
    marginTop: 15,
  },
  icon: {
    color: "#f094c0",
    fontSize: 75,
  },
});

export default styles;
