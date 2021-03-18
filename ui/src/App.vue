<template>
  <v-app>
    <v-row>
      <v-col cols="2" style="padding: 0">
        <MainMenu/>
      </v-col>
      <v-col cols="10" style="padding: 0">
        <NavBar/>
        <v-main style="margin: 5px">
          <router-view></router-view>
        </v-main>
      </v-col>
    </v-row>
  </v-app>
</template>

<script>

import MainMenu from "./components/layout/MainMenu";
import NavBar from "./components/layout/NavBar";

export default {
  name: 'App',
  components: {
    MainMenu,
    NavBar
  }
};
</script>
