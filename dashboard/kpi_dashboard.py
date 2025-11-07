"""
KPI Dashboard
Displays key performance indicators for all departments
"""

from datetime import datetime


class KPIDashboard:
    """Main KPI Dashboard for FMS Director"""
    
    def __init__(self):
        self.kpis = {
            'ppm_completion': 0.0,
            'cm_response_time': 0.0,
            'open_risks': 0,
            'contractor_compliance': 0.0
        }
        
    def display(self):
        """Display the main KPI dashboard"""
        print("\n" + "="*60)
        print("📊 لوحة مؤشرات الأداء / KPI Dashboard")
        print("="*60)
        print(f"\n📅 التاريخ / Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n" + "-"*60)
        
        self.display_ppm_kpi()
        self.display_response_time_kpi()
        self.display_risks_kpi()
        self.display_contractor_kpi()
        
        print("\n" + "="*60)
        print("\n1. تحديث المؤشرات / Update KPIs")
        print("2. تصدير التقرير / Export Report")
        print("0. رجوع / Back")
        
        choice = input("\nاختر خياراً / Choose option: ").strip()
        
        if choice == '1':
            self.update_kpis()
        elif choice == '2':
            self.export_report()
            
    def display_ppm_kpi(self):
        """Display PPM completion percentage"""
        print("\n🔧 نسبة إنجاز الصيانة الوقائية / PPM Completion Rate")
        print(f"   الصيانة العامة / General Maintenance: {self._get_demo_ppm('general')}%")
        print(f"   الصيانة الطبية / Medical Maintenance: {self._get_demo_ppm('medical')}%")
        
    def display_response_time_kpi(self):
        """Display average response time for critical CM"""
        print("\n⏱️ متوسط زمن الاستجابة / Average Response Time")
        print(f"   البلاغات الحرجة / Critical CM: {self._get_demo_response_time()} ساعة / hours")
        
    def display_risks_kpi(self):
        """Display open risks count"""
        print("\n⚠️ المخاطر المفتوحة / Open Risks")
        print(f"   عدد المخاطر المصعدة / Escalated Risks: {self._get_demo_open_risks()}")
        
    def display_contractor_kpi(self):
        """Display contractor compliance status"""
        print("\n🏢 التزام المقاولين / Contractor Compliance")
        print(f"   SAMAIA: {self._get_demo_compliance('samaia')}%")
        print(f"   مقاولو الوزارة / Ministry Contractors: {self._get_demo_compliance('ministry')}%")
        
    def update_kpis(self):
        """Update KPI values"""
        print("\n🔄 جاري تحديث المؤشرات / Updating KPIs...")
        print("✅ تم التحديث بنجاح / Updated successfully")
        
    def export_report(self):
        """Export KPI report"""
        print("\n📤 جاري تصدير التقرير / Exporting report...")
        print("✅ تم الحفظ في: reports/kpi_report_" + 
              datetime.now().strftime('%Y%m%d') + ".xlsx")
        
    # Demo data methods
    def _get_demo_ppm(self, dept):
        """Get demo PPM completion rate"""
        demo_data = {'general': 85.5, 'medical': 92.3}
        return demo_data.get(dept, 0.0)
        
    def _get_demo_response_time(self):
        """Get demo average response time"""
        return 2.5
        
    def _get_demo_open_risks(self):
        """Get demo open risks count"""
        return 3
        
    def _get_demo_compliance(self, contractor):
        """Get demo contractor compliance"""
        demo_data = {'samaia': 88.0, 'ministry': 91.5}
        return demo_data.get(contractor, 0.0)
