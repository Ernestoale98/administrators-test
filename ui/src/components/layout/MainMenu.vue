<template>
  <v-list min-width="100%" dense>
    <v-list-item style="text-align: center">
      <v-list-item-avatar class="mx-auto">
        <v-img src="https://www.gravatar.com/avatar/www.prueba.test.com"></v-img>
      </v-list-item-avatar>
    </v-list-item>
    <v-list-item-group
        v-model="selectedItem"
        color="primary">
      <v-list-item
          v-for="(item, i) in items"
          :key="i">
        <v-list-item-icon>
          <v-icon v-text="item.icon"></v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title v-text="item.text"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list-item-group>
  </v-list>
</template>

<script>
export default {
  name: 'MainMenu',
  data: () => ({
    selectedItem: 1,
    items: [
      {text: 'Real-Time', icon: 'mdi-clock'},
      {text: 'Audience', icon: 'mdi-account'},
      {text: 'Conversions', icon: 'mdi-flag'},
    ],
  }),
}
</script>