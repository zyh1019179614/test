<template>
    <div>
        <strong>Default Size:</strong>
        <br><br>
        <List header="Header" footer="Footer" border>
            <ListItem>This is a piece of text.</ListItem>
            <ListItem>This is a piece of text.</ListItem>
            <ListItem>This is a piece of text.</ListItem>
        </List>
        <br>
        <strong>Small Size:</strong>
        <br><br>
        <List header="Header" footer="Footer" border size="small">
            <ListItem>This is a piece of text.</ListItem>
            <ListItem>This is a piece of text.</ListItem>
            <ListItem>This is a piece of text.</ListItem>
        </List>
        <br>
        <strong>Large Size:</strong>
        <br><br>
        <List header="Header" footer="Footer" border size="large">
            <ListItem>This is a piece of text.</ListItem>
            <ListItem>This is a piece of text.</ListItem>
            <ListItem>This is a piece of text.</ListItem>
        </List>
    </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
