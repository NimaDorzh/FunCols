<script setup>
import { RouterLink, RouterView } from "vue-router";
import { ref } from 'vue';


const menuOpen = ref(false);
function toggleMenu() {
  menuOpen.value = !menuOpen.value;
}

// Функция для закрытия меню при нажатии на элемент
function closeMenu() {
  menuOpen.value = false;
}


</script>

<template>
  <div id="app">
    <!-- Навигационное меню -->
    <header>
      <nav class="navbar" @mouseleave="closeMenu"> 
        <div class="logo">
          <img src="./assets/logo.svg" alt="Logo" width="50" height="50" />
        </div>
        <div class="menu-icon" @click="toggleMenu">
          <!-- Бургер-меню -->
          <span></span>
          <span></span>
          <span></span>
        </div>

        <ul class="list" :class="{ 'show': menuOpen }">
          <li class="list-item"><router-link to="/">Главная</router-link></li>
          <li class="list-item"><router-link to="/register">Регистрация</router-link></li>
          <li class="list-item"><router-link to="/login">Вход</router-link></li>
          <li class="list-item"><router-link to="/about">О нас</router-link></li>
          <li class="list-item"><router-link to="/contacts">Контакты</router-link></li>
        </ul>
      </nav>
    </header>

    <!-- Основной контент -->
    <main class="main-content">
      <div class="content-container">
        <router-view></router-view> <!-- Здесь будут отображаться страницы в зависимости от маршрута -->
      </div>
    </main>

    <!-- Футер -->
    <footer>
      <p>© 2024 Ваше приложение. Все права защищены.</p>
    </footer>
  </div>
</template>

<style scoped>
/* Базовые стили */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}

#app {
  max-width: 1920px;
  margin: 0 auto;
  padding: 0;
}

/* Навигация */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  padding: 10px 20px;
}

.logo img {
  max-width: 100px;
}

.menu-icon {
  display: none;
  flex-direction: column;
  cursor: pointer;
}

.menu-icon span {
  background-color: white;
  height: 3px;
  margin: 5px 0;
  width: 25px;
}

.list {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-around;
  flex: 1;
}

.list-item {
  display: inline-block;
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

/* Адаптивные стили */
@media screen and (max-width: 1920px) {
  .logo img {
    max-width: 75px; /* Уменьшение логотипа для Full HD */
  }

  .list-item a {
    padding: 10px 15px; /* Уменьшение отступов для Full HD */
  }
}

@media screen and (max-width: 1366px) {
  .logo img {
    max-width: 50px; /* Уменьшение логотипа для HD */
  }

  .list-item a {
    padding: 8px 12px; /* Уменьшение отступов для HD */
  }
}

@media screen and (max-width: 1024px) {
  .list {
    display: none;
    flex-direction: column;
    position: absolute;
    top: 60px;
    left: 0;
    right: 0;
    background-color: #333;
  }

  .list.show {
    display: flex;
  }

  .menu-icon {
    display: flex;
  }

  .list-item {
    text-align: center;
    width: 100%;
  }

  .list-item a {
    padding: 14px;
  }

  .logo img {
    max-width: 40px; /* Уменьшение логотипа для мобильных версий */
  }
}

/* Основной контент */
.main-content {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 80vh; /* Основной контент занимает 80% высоты экрана */
  background-color: #fff;
  padding: 20px;
}

.content-container {
  width: 100%;
  max-width: 1200px; /* Ограничение ширины основного контента */
  margin: 0 auto; /* Центрирование контейнера контента */
  padding: 20px;
  background-color: #f8f8f8;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); /* Легкая тень для контента */
  border-radius: 8px;
}

/* Футер */
footer {
  width: 100%; /* Ширина футера на 100% */
  background-color: #333;
  color: white;
  text-align: center;
  padding: 10px 0;
  margin-top: 20px;
  position: relative;
  bottom: 0;
}
</style>
