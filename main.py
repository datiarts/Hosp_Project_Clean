#!/usr/bin/env python3
"""
AMP - Accountability & Operations Management Program
Main entry point for the Hospital Facility Management System
"""

import sys
from datetime import datetime
from modules.general_maintenance import GeneralMaintenanceModule
from modules.safety_security import SafetySecurityModule
from modules.medical_maintenance import MedicalMaintenanceModule
from modules.support_services import SupportServicesModule
from dashboard.kpi_dashboard import KPIDashboard


class AMPApplication:
    """Main application class for AMP system"""
    
    def __init__(self):
        self.modules = {
            'general_maintenance': GeneralMaintenanceModule(),
            'safety_security': SafetySecurityModule(),
            'medical_maintenance': MedicalMaintenanceModule(),
            'support_services': SupportServicesModule()
        }
        self.dashboard = KPIDashboard()
        
    def display_main_menu(self):
        """Display main menu options"""
        print("\n" + "="*60)
        print("🏥 AMP - نظام إدارة عمليات المرافق والسلامة")
        print("   Accountability & Operations Management Program")
        print("="*60)
        print("\n📋 القائمة الرئيسية / Main Menu:")
        print("\n1. الصيانة العامة / General Maintenance")
        print("2. الأمن والسلامة / Safety & Security")
        print("3. الصيانة الطبية / Medical Maintenance")
        print("4. الخدمات المساندة / Support Services")
        print("5. لوحة المؤشرات / KPI Dashboard")
        print("6. التقارير / Reports")
        print("0. خروج / Exit")
        print("\n" + "="*60)
        
    def run(self):
        """Main application loop"""
        print(f"\n🚀 تشغيل النظام - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        while True:
            self.display_main_menu()
            choice = input("\nاختر من القائمة / Choose an option: ").strip()
            
            if choice == '1':
                self.modules['general_maintenance'].run()
            elif choice == '2':
                self.modules['safety_security'].run()
            elif choice == '3':
                self.modules['medical_maintenance'].run()
            elif choice == '4':
                self.modules['support_services'].run()
            elif choice == '5':
                self.dashboard.display()
            elif choice == '6':
                self.generate_reports()
            elif choice == '0':
                print("\n👋 شكراً لاستخدام النظام / Thank you for using AMP")
                sys.exit(0)
            else:
                print("\n❌ اختيار غير صحيح / Invalid choice")
                
    def generate_reports(self):
        """Generate comprehensive reports"""
        print("\n📊 جاري إنشاء التقارير / Generating Reports...")
        print("\n1. التقرير الأسبوعي / Weekly Report")
        print("2. التقرير الشهري / Monthly Report")
        print("3. ملخص تنفيذي / Executive Summary")
        print("0. رجوع / Back")
        
        choice = input("\nاختر نوع التقرير / Choose report type: ").strip()
        if choice in ['1', '2', '3']:
            print(f"\n✅ التقرير قيد الإنشاء / Report is being generated...")
            # Report generation logic will be implemented
        

if __name__ == "__main__":
    app = AMPApplication()
    app.run()
