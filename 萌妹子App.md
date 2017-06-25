java1.8
```
buildscript {
    repositories {
        mavenCentral()
        maven { url "https://jitpack.io" }
    }
    dependencies {
        classpath 'me.tatarka:gradle-retrolambda:3.2.5'
    }
}
apply plugin: 'me.tatarka.retrolambda'
```