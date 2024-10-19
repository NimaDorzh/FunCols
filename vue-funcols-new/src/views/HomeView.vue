<template>
 
</template>

<script>
export default {
  name: 'TopMenu'
};
</script>

<style scoped>
.navbar {
  width: 100%;
  background-color: #333;
  padding: 10px;
}

.list {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-around;
}

.list-item {
  display: inline;
}

.list-item a {
  color: white;
  text-decoration: none;
  padding: 14px 20px;
  display: block;
}

.list-item a:hover {
  background-color: #575757;
  border-radius: 4px;
}
</style>
