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
          <v-list-item-title>
            <router-link :to="item.route" v-text="item.text"></router-link>
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list-item-group>
  </v-list>
</template>

<script>
export default {
  name: 'MainMenu',
  data: () => ({
    selectedItem: 0,
    items: [
      {text: 'Dashboard', icon: 'mdi-clock', route: '/dashboard'},
      {text: 'Administrators', icon: 'mdi-account', route: 'administrators'},
    ],
  }),
}
</script>