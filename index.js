const puppeteer = require("puppeteer");
const delay = ms => new Promise(res => setTimeout(res, ms));
//const getI = () => new Promise(res => );
(async () => {
  //  console.log(process.argv);
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  await page.goto(process.env.CANDY_URL);

  console.log(process.env.CODE1);
  await page.type("input#VisitnoAuthName.form-control", process.env.CODE1);
  await page.type("input#VisitnoAuthVisitno.form-control", process.env.CODE2);
  await page.type(
    "select#VisitnoAuthYear.form-control.selectpicker",
    process.env.CANDY_BIRTHDAY_YEAR
  );
  await page.keyboard.press("Enter");
  await page.type(
    "select#VisitnoAuthMonthMonth.form-control.selectpicker",
    process.env.CANDY_BIRTHDAY_MONTH
  );
  await page.keyboard.press("Enter");
  await page.type(
    "select#VisitnoAuthDayDay.form-control.selectpicker",
    process.env.CANDY_BIRTHDAY_DAY
  );
  await page.keyboard.press("Enter");
  await page.focus("button.btn.btn-warning.auth-btn.center-block");
  await page.keyboard.press("Enter");
  await page.waitForNavigation();

  await page.focus(
    "button.btn.btn-lg.btn-next.btn-warning.btn-block.center-block"
  );
  await page.keyboard.press("Enter");
  await page.waitForNavigation();

  let arr = await page.$$eval(
    "a.btn.btn-lg.btn-next.btn-warning.covid19_move_plan_detail",
    (arr, i) => {
      arr[i].focus();
    },
    Number(process.argv[process.argv.length - 1])
  );
  await page.keyboard.press("Enter");
  await page.waitForNavigation();

  await page.screenshot({
    path: `screenshots/page_top_${process.argv[process.argv.length - 1]}.png`,
    format: "a4"
  });
  await page.evaluate(() => {
    window.scrollBy(0, 2 * window.innerHeight);
  });
  //  await delay(10000);
  await page.screenshot({
    path: `screenshots/page_bottom_${
      process.argv[process.argv.length - 1]
    }.png`,
    format: "a4"
  });
  await browser.close();
})();
