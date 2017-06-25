##3. 工具类封装：

###3.1 Log 封装成代号L

日志：主要在控制台打印成一些我们运行中所产生的一些信息，我们把Log分成五个等级：
	
	1. static Level DEBUG:
	细粒度信息事件,对于调试应用程序是非常有帮助的
	2. static Level INFO
	粗粒度级别上，突出强调应用程序的运行过程
	3. static Level WARN
	潜在错误情形，会导致应用程序的退出
	4. static Level ERROR
	虽然发生错误事件，但是不影响系统的继续运行
	5. static Level FATAl
	严重的错误事件将导致应用程序的退出

LOG 应该有一个统计的开关和TAG
```
Log.i(TAG,TEXT)
```
封装完整代码
```java
package com.mtianyan.mtianyan001.utils;

import android.util.Log;

/**
 * 项目名：Mtianyan001
 * 包名：com.mtianyan.mtianyan001.utils
 * 文件名：L
 * 作者：mtianyan
 * 创建时间：2017/6/1 12:14
 * 描述：LOG封装
 */
public class L {
    //开关
    public static final boolean DEBUG = true;
    //TAG
    public static final String TAG = "mtianyan001";

    //实现五个等级 D I W E F

    public static void d(String test) {
        if (DEBUG) {
            Log.d(TAG, test);
        }
    }
    public static void i(String test){
        if(DEBUG){
            Log.i(TAG,test);
        }
    } public static void w(String test){
        if(DEBUG){
            Log.w(TAG,test);
        }
    }public static void e(String test){
        if(DEBUG){
            Log.e(TAG,test);
        }
    }public static void f(String test){
        if(DEBUG){
            Log.wtf(TAG,test);
        }
    }
}

```
###3.2 封装SharePreferences

android数据四种存储方式

SharePreferences xml key-value
存储简单的配置信息

对象本身只能获取数据，而不支持存储和修改，存储修改是通过Editor对象实现的

1. 根据context获取SharePreferen对象
2. 利用edit()方法获取Editor对象
3. 通过Editor对象存储key-value键值对数据
4. 通过commit()方法提交

封装所需要注意的点：
    
    1. 定义存取方式：get put
    2. 明确数据类型 int/String/Boolean
    3. 定义删除功能: 单个/全部

封装SharePreferences的完整代码
```java
package com.mtianyan.mtianyan001.utils;

import android.content.Context;
import android.content.SharedPreferences;

/**
 * 项目名：Mtianyan001
 * 包名：com.mtianyan.mtianyan001.utils
 * 文件名：ShareUtils
 * 作者：mtianyan
 * 创建时间：2017/6/1 15:42
 * 描述：封装SharePreferences
 */
public class ShareUtils {
    //原始方法存取
//    private  void test(Context mcontext){
//        SharedPreferences sp = mcontext.getSharedPreferences("config",Context.MODE_PRIVATE);
//        SharedPreferences.Editor editor =sp.edit();
//        sp.getString("key","未获取到值");
//
//        editor.putString("key","value");
//
//        editor.commit();
//
//
//    }
    public static final String NAME = "config";

    //键 值
    public static  void putString(Context mcontext,String key,String value){
        SharedPreferences sp =mcontext.getSharedPreferences(NAME,Context.MODE_PRIVATE);
        sp.edit().putString(key,value).commit();
    }
    //键 默认值
    public static String getString(Context mcontext,String key,String defvalue){
        SharedPreferences sp = mcontext.getSharedPreferences(NAME,Context.MODE_PRIVATE);
        return sp.getString(key,defvalue);

    } //键 值
    public static  void putInt(Context mcontext,String key,int value){
        SharedPreferences sp =mcontext.getSharedPreferences(NAME,Context.MODE_PRIVATE);
        sp.edit().putInt(key,value).commit();
    }
    //键 默认值
    public static int getInt(Context mcontext,String key,int defvalue){
        SharedPreferences sp = mcontext.getSharedPreferences(NAME,Context.MODE_PRIVATE);
        return sp.getInt(key,defvalue);

    } //键 值
    public static  void putBoolean(Context mcontext,String key,boolean value){
        SharedPreferences sp =mcontext.getSharedPreferences(NAME,Context.MODE_PRIVATE);
        sp.edit().putBoolean(key,value).commit();
    }
    //键 默认值
    public static Boolean getBoolean(Context mcontext,String key,boolean defvalue){
        SharedPreferences sp = mcontext.getSharedPreferences(NAME,Context.MODE_PRIVATE);
        return sp.getBoolean(key,defvalue);

    }

    //删除单个
    public static void deleShare(Context mcontext,String key){
        SharedPreferences sp = mcontext.getSharedPreferences(NAME,Context.MODE_PRIVATE);
        sp.edit().remove(key).commit();
    }

    //删除全部
    public static void deleAll(Context mcontext){
        SharedPreferences sp = mcontext.getSharedPreferences(NAME,Context.MODE_PRIVATE);
        sp.edit().clear().commit();
    }

}

```

###3.3 首页跳转逻辑

首页用来做：
    1. 展示公司/个人的logo
    2. 广告
    3. 初始化数据
    4. 自定义字体

1. 注册splashactivity成为入口

```xml
 <!--splash闪屏页设置成入口-->
        <activity android:name=".ui.SplashActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <!--设置-->
        <activity android:name=".ui.SettingActivity"
            android:label="@string/text_setting">
        </activity>
        <!--主页-->
        <activity android:name=".MainActivity"
            ></activity>
```

2. 延时两秒用handler来做


```java
 private Handler handler = new Handler(){
        @Override
        public void handleMessage(Message msg) {
            super.handleMessage(msg);
            switch (msg.what){
                case StaticClass.HANDLER_SPLASH:
                //判断程序是否是第一次运行
                if (isFirst()){
                    startActivity(new Intent(SplashActivity.this, GuideActivity.class));
                }else{
                    startActivity(new Intent(SplashActivity.this, MainActivity.class));
                }
                    finish();
                    break;
            }
        }

    };
handler.sendEmptyMessageDelayed(StaticClass.HANDLER_SPLASH,2000);

```
整体流程：
第一次进来发消息进行延时，判断是否第一次运行
如果第一次运行，就使用引导页

3. 修改values/style.xml全屏引导





###3.4 腾讯Bugly



###3.5 登录注册
bmob
3-3 22分钟总结