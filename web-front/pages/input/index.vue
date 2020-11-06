<template>
  <div class="container">
    <div>
        <textarea v-model="message" placeholder="add multiple lines"></textarea>
        <InkButton />
        <button></button>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

</style>
